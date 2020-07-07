from __future__ import annotations

import logging
from typing import List
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup
import requests

from article.article import Article

TOP_READ = 'https://www.delfi.ee/archive/loetumad/'


def parse_id(article_url: str) -> str:
    return parse_qs(urlparse(article_url).query)['id'][0]


def extract_url(article) -> str:
    return (Navigator(article)
            .anchor()
            .href()
            .get())


def extract_title(article) -> str:
    return (Navigator(article)
            .div()
            .anchor()
            .text()
            .get())


def construct(article) -> Article:
    url = extract_url(article)

    return Article(article_id=parse_id(url),
                   title=extract_title(article),
                   url=url)


class ArticleScraper:

    def __init__(self, source=TOP_READ):
        logging.info('Scraping articles from {}'.format(source))

        self.soup = BeautifulSoup(features='html.parser',
                                  markup=requests.get(source).content)

    def get(self) -> List[Article]:
        return [construct(article) for article in self.soup.find_all('article')]


class Navigator:

    def __init__(self, article):
        self.article = article
        self.target = None

    def get(self):
        return self.target

    def div(self) -> Navigator:
        self.target = self.get_target().find('div')
        return self

    def clazz(self, clazz_name: str) -> Navigator:
        self.target = self.get_target().find({'class', clazz_name})
        return self

    def attribute(self, attribute: str) -> Navigator:
        self.target = self.get_target()[attribute]
        return self

    def anchor(self) -> Navigator:
        self.target = self.get_target().find('a')
        return self

    def text(self) -> Navigator:
        self.target = self.get_target().text
        return self

    def href(self) -> Navigator:
        self.target = self.get_target()['href']
        return self

    def get_target(self):
        if self.target is None:
            return self.article
        return self.target
