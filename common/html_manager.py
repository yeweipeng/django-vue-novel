import requests
from bs4 import BeautifulSoup


def get_html(url, params=None, timeout=10):
	response = requests.get(url, params=params, timeout=timeout)
	response.encoding = 'utf-8'
	return response.text


def parse_only_field_text(html_res, selected):
	return parse_only_field(html_res, selected).get_text()


def parse_only_field(html_res, selected):
	soup = BeautifulSoup(html_res, 'html.parser')
	return soup.select(selected)[0]

def parse_field_list(html_res, selected):
	soup = BeautifulSoup(html_res, 'html.parser')
	return soup.select(selected)
