# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BookLikeTab(models.Model):
  user_id = models.IntegerField()
  book_id = models.CharField(max_length=16)
  book_name = models.CharField(max_length=32)
  book_img_url = models.CharField(max_length=256)
  last_read_chapter_id = models.IntegerField()
  last_read_chapter_name = models.CharField(max_length=32)
  latest_chapter_id = models.IntegerField()
  flag = models.IntegerField()
