import schema
import json
from functools import wraps
from django import forms, http
from . import log
from .error_code import ErrorCodeField, CommonErrorCode

def response_parse_fail(_, msg):
	return {
		'retcode': CommonErrorCode.PARAMS_INVALID,
		'retmsg': msg
	}


def parse_params(form, method='POST', data_format='FORM', error_handler=response_parse_fail, needs_unescape=True):
	def _parse_params(func):
		@wraps(func)
		def _func(request, *args, **kwargs):
			if request.method != method:
				log.warning('view_method_error|url=%s,method=%s', request.get_full_path(), request.method)
				return error_handler(request, '{method} is not allow'.format(method=request.method))
			if data_format == 'XML':
				try:
					xml_data = etree.XML(request.body)
				except:
					log.warning('view_params_error|format=xml,url=%s,body=%s', request.get_full_path(), request.body)
					return error_handler(request, "parse xml fail")
				if not form(xml_data):
					log.warning('view_params_schema_error|format=xml,url=%s,error=%s,body=%s', request.get_full_path(), form.error_log, request.body)
					return error_handler(request, form.error_log)
				data = {'xml_data': xml_data}
			elif data_format == 'JSON':
				if isinstance(form, schema.Schema):
					data = form.validate(request.body)
				elif inspect.isclass(form) and issubclass(form, forms.Form):
					data = request.body
					if needs_unescape:
						data = data.decode('string_escape')
					dataform = form(json.loads(data))
					if not dataform.is_valid():
						log.warning('view_params_error|format=form,url=%s,error=%s,body=%s', request.get_full_path(), dataform.errors.__repr__(), request.body)
						return error_handler(request, dataform.errors.__repr__())
					data = dataform.cleaned_data
				else:
					params_errors = [e.message for e in form.iter_errors(json.loads(request.body))]
					if params_errors:
						log.warning('view_params_error|format=json,url=%s,error=%s,body=%s', request.get_full_path(), ';'.join(params_errors), request.body.encode('utf-8'))
						return error_handler(request, ';'.join(params_errors))
					data = json.loads(request.body)
			else:
				if method == 'GET':
					dataform = form(request.GET)
				elif data_format == 'MULTIPART':
					dataform = form(request.POST, request.FILES)
				else:
					dataform = form(request.POST)

				if not dataform.is_valid():
					request_body = request.body if hasattr(request, 'body') else ''
					log.warning('view_params_error|format=form,url=%s,error=%s,body=%s', request.get_full_path(), dataform.errors.__repr__(), request_body)
					return error_handler(request, dataform.errors.__repr__())
				data = dataform.cleaned_data
			return func(request, data, *args, **kwargs)

		return _func

	return _parse_params


def json_rsp(func):
	@wraps(func)
	def _func(request, *args, **kwargs):
		resp = func(request, *args, **kwargs)
		if isinstance(resp, http.HttpResponse):
			return resp

		if isinstance(resp, ErrorCodeField):
			return http.HttpResponse(json.dumps({'retcode': resp, 'retmsg': resp.message}), content_type='application/json; charset=utf-8')

		if 'retcode' not in resp:
			resp['retcode'] = CommonErrorCode.SUCCESS
			resp['retmsg'] = CommonErrorCode.SUCCESS.message
		return http.HttpResponse(json.dumps(resp), content_type='application/json; charset=utf-8')
	return _func


def re_map_keys(rows, update_map={}, del_list=[]):
	for row in rows:
		for name in row.keys():
			if name in update_map:	
				row[update_map[name]] = row[name]
				del row[name]
			if name in del_list:
				row.pop(name, None)
