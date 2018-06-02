from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^get_like_book_list/$', views.get_like_book_list),
	url(r'^get_chapter/$', views.get_chapter),
	url(r'^get_chapter_list/$', views.get_chapter_list),
]
