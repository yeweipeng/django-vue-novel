# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from common.api_utils import json_rsp, parse_params
from . import forms
from . import book_manager

# Create your views here.

@json_rsp
@parse_params(forms.BookLikeListForm, 'GET')
def get_books(request, data):
  return {"data" : book_manager.get_like_book_list(1)}

