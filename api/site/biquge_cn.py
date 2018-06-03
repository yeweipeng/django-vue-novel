import common.html_manager as html_manager
import re

def get_search_url():
	return 'http://www.biquge.com.cn/search.php'


def get_chapter_url(book_id, chapter_id=None):
	if chapter_id is None:
		return 'http://www.biquge.com.cn/book/{book_id}/'.format(book_id=book_id)
	else:
		return 'http://www.biquge.com.cn/book/{book_id}/{chapter_id}.html'.format(book_id=book_id, chapter_id=chapter_id)


def search(kw):
	html_res = html_manager.get_html(get_search_url(), {'keyword': kw})
	books = html_manager.parse_field_list(html_res, '.result-item')
	res = []
	for book in books:
		link = book.select('.result-game-item-info-tag-item')[0]
		hrefs = link.attrs['href'].split('/')
		res.append({
			'id': hrefs[4],
			'last_read_chapter_id': hrefs[5][0:-6],
			'name': book.select('.result-item-title')[0].text,
			'has_latest': False,
			'last_read_chapter_name': link.text,
			'img_url': book.select('img')[0].attrs['src'],
			'is_save': False
		})
	return res


def get_novel(book_id, chapter_id):
	url = get_chapter_url(book_id, chapter_id)
	html_res = html_manager.get_html(url)
	novel = {
		'title': html_manager.parse_only_field_text(html_res, '.bookname h1'),
		'content': html_manager.parse_only_field_text(html_res, '#content')
	}
	novel['content'] = ' ' * 4 +re.sub(ur'\u00a0{4}', '\n' + ' ' * 4, novel['content'][4:])
	return novel


def get_chapter_list(book_id):
	dirs = []	
	url = get_chapter_url(book_id)
	try:
		html_res = html_manager.get_html(url, timeout=5)	
	except ConnectionError:
		return dirs

	links = html_manager.parse_field_list(html_res, 'dd a')
	for link in links:
		dirs.append({
			'text': link.text,
			'chapter_id': int(link.attrs['href'].split('/')[3][0:-5])
		})
	return dirs
