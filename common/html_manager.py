import requests
from bs4 import BeautifulSoup


def get_html(url, params=None):
	response = requests.get(url, params=params, timeout=10)
	response.encoding = 'gb2312'
	return response.text


def parse_only_field_text(html_res, selected):
	soup = BeautifulSoup(html_res, 'html.parser')
	return soup.select(selected)[0].text

def parse_field_list(html_res, selected):
	soup = BeautifulSoup(html_res, 'html.parser')
	return soup.select(selected)
