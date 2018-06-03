# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from common.api_utils import json_rsp, parse_params
from . import forms
from . import book_manager


@json_rsp
@parse_params(forms.BookLikeListForm, 'GET')
def get_like_book_list(request, data):
	book_list = book_manager.get_like_book_list(1)
	for book in book_list:
		book['has_latest'] = book_manager.get_latest_chapter_info(book['id'], book['last_read_chapter_id'])
	return {"data" : book_list}


@json_rsp
@parse_params(forms.ChapterForm, 'GET')
def get_chapter(requset, data):
	return book_manager.get_chapter_content(data['book_id'], data['chapter_id'])


@json_rsp
@parse_params(forms.ChapterListForm, 'GET')
def get_chapter_list(requset, data):
	return book_manager.get_chapter_list(data['book_id'])


@json_rsp
@parse_params(forms.SearchForm, 'GET')
def search(requset, data):
	return {'data' : book_manager.search_book(data['search_word'])}

@json_rsp
@parse_params(forms.LikeBookForm, 'GET')
def like_book(requset, data):
	return book_manager.like_book(data)

@json_rsp
def set_token(request):
	from django.http import HttpResponse
	import uuid
	token = str(uuid.uuid4())
	rsp = HttpResponse(token)
	rsp.set_cookie('TOKEN', token)
	return rsp