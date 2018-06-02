from django.forms import Form
from django import forms

class BookLikeListForm(Form):
	pass


class ChapterForm(Form):
	book_id = forms.CharField(required=True)
	chapter_id = forms.IntegerField(min_value=0, required=True)


class ChapterListForm(Form):
	book_id = forms.CharField(required=True)
	