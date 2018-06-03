from django.forms import Form
from django import forms

class BookLikeListForm(Form):
	pass


class ChapterForm(Form):
	book_id = forms.CharField(required=True)
	chapter_id = forms.IntegerField(min_value=0, required=True)


class ChapterListForm(Form):
	book_id = forms.CharField(required=True)


class SearchForm(Form):
	search_word = forms.CharField(required=True)


class LikeBookForm(Form):
	id = forms.CharField(required=True)
	name = forms.CharField(required=True)
	img_url = forms.CharField(required=True)
	last_read_chapter_id = forms.CharField(required=True)
	last_read_chapter_name = forms.CharField(required=True)
