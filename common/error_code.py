import six

class ErrorCodeField(int):
	def __new__(cls, error_code, message=u""):
		obj = int.__new__(cls, error_code)
		obj.message = message
		return obj


class ErrorCodeMetaClass(type):
    def __new__(cls, name, bases, namespace):
        code_message_map = {}
        for k, v in namespace.items():
            if getattr(v, '__class__', None) and isinstance(v, ErrorCodeField):
                if code_message_map.get(v):
                    raise ValueError("duplicated codde {0} {1}".format(k, v))
                code_message_map[v] = getattr(v, 'message', "")
        namespace["CODE_MESSAGE_MAP"] = code_message_map
        return type.__new__(cls, name, bases, namespace)


class BaseErrorCode(six.with_metaclass(ErrorCodeMetaClass)):
    CODE_MESSAGE_MAP = NotImplemented


class CommonErrorCode(BaseErrorCode):
    PARAMS_INVALID = ErrorCodeField(-1, u"params invalid")
    SUCCESS = ErrorCodeField(0, u"success")
