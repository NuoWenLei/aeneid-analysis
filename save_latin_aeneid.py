import requests
from bs4 import BeautifulSoup

def main():
	url = "https://www.gutenberg.org/files/227/227-h/227-h.htm"

	r = requests.get(url)

	soup = BeautifulSoup(r.text, "html.parser")

	