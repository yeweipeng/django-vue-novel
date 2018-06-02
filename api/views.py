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