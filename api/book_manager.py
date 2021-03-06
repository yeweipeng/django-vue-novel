from .models import BookLikeTab
from common.api_utils import re_map_keys
from common.error_code import CommonErrorCode
import api.site.biquge_cn as noval_manager

def search_book(search_word):
	return noval_manager.search(search_word)


def get_like_book_list(user_id):
	book_list = list(BookLikeTab.objects.filter(user_id=user_id, flag=1).values())
	update_map = {
		'book_id': 'id',
		'book_name': 'name',
		'book_img_url': 'img_url',
		'flag': 'is_save'
	}
	del_list = ['user_id']
	re_map_keys(book_list, update_map, del_list)
	for row in book_list:
		row['is_save'] = row['is_save'] == 1
	return book_list


def get_chapter_content(book_id, chapter_id):
	return noval_manager.get_novel(book_id, chapter_id)


def get_chapter_list(book_id):
	return {
		'chapters': noval_manager.get_chapter_list(book_id),
	}


def get_latest_chapter_info(book_id, now_chapter_id):
	chapter_list = noval_manager.get_chapter_list(book_id)
	chapter_sum = len(chapter_list)
	now_pos = [index for index in range(chapter_sum) if chapter_list[index]['chapter_id'] == now_chapter_id]
	if len(now_pos) == 0 or now_pos[0] + 1 == chapter_sum:
		return False
	else:
		return True

def like_book(data):
	update_map = {
		'id': 'book_id',
		'name': 'book_name',
		'img_url': 'book_img_url',
	}
	re_map_keys([data], update_map)
	data['user_id'] = 1
	data['latest_chapter_id'] = 0
	data['flag'] = 1
	book_like_item = BookLikeTab(**data)
	book_like_item.save()
	return CommonErrorCode.SUCCESS
