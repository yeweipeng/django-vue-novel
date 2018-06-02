import common.html_manager as html_manager

def get_chapter_url(book_id, chapter_id=None):
	if chapter_id is None:
		return 'http://www.biquge.com.tw/{book_id}/'.format(book_id=book_id)
	else:
		return 'http://www.biquge.com.tw/{book_id}/{chapter_id}.html'.format(book_id=book_id, chapter_id=chapter_id)


def get_novel(book_id, chapter_id):
	url = get_chapter_url(book_id, chapter_id)
	html_res = html_manager.get_html(url)
	return {
		'title': html_manager.parse_only_field_text(html_res, '.bookname h1'),
		'content': html_manager.parse_only_field_text(html_res, '#content')
	}


def get_chapter_list(book_id):
	url = get_chapter_url(book_id)
	html_res = html_manager.get_html(url)	
	links = html_manager.parse_field_list(html_res, 'dd a')
	dirs = []
	for link in links:
		dirs.append({
			'text': link.text,
			'chapter_id': int(link.attrs['href'].split('/')[2][0:-5])
		})
	return dirs
