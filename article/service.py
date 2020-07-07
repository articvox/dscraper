from typing import List

from article.article import Article
from article.scraper import ArticleScraper


def get_articles() -> List[Article]:
    return ArticleScraper().get()
