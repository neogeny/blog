# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import re
import html
from pathlib import Path
from urllib.parse import urlparse
import pypandoc
from bs4 import BeautifulSoup as BS
import dateutil.parser


THIS_DIR = Path(__file__).parent
ROOT_DIR = THIS_DIR.parent
POSTS_DIR = ROOT_DIR / 'content'

IMAGE_RE = r'image:: *(http:.*?)$'

BLOG_HEADER = '''\

:date: %s
:slug: %s
:author: Apalala

.. :tags:
.. :category:
.. :summary:
'''


def fix_images(content):
    urls = re.findall(IMAGE_RE, content, flags=re.MULTILINE)
    for url in urls:
        filename = urlparse(url).path.split('/')[-1]
        filename = Path(filename.replace('.bmp', '.jpg'))
        content = re.sub(IMAGE_RE, 'image:: /images/%s' % str(filename), content, flags=re.MULTILINE)
        content = re.sub(r'^ *:target:.*?$', '', content, flags=re.MULTILINE)
    return content


def bsoup():
    with open('etc/blog-06-01-2014.xml') as f:
        xml = f.read()
    soup = BS(xml)
    soup = BS(soup.prettify())
    entries = soup.html.body.feed.find_all('entry')
    posts = [e for e in entries if e.category['term'].endswith('post')]

    slugs = set()
    for e in posts:
        title = e.title.text.strip()
        date = dateutil.parser.parse(e.published.text.strip())
        date = date.strftime('%Y-%m-%d')

        slug = title.lower()
        slug = slug.translate(
            str.maketrans(
                '&%^$@#"!¿?:/., (áéíóúñ' + "'",
                '----------------aeioun' + "-",
                ")"
            )
        )
        slug = slug.replace('--', '-')
        slug = slug.strip('-')
        if slug in slugs:
            for i in range(1, 10):
                newslug = '%s-%d' % (slug, i)
                if newslug not in slugs:
                    slug = newslug
                    break
        slug = slug.replace('--', '-')
        slugs.add(slug)
        print(slug)

        content = html.unescape(e.content.text)
        content = '<h1>%s</h1>\n' % title + content
        content = pypandoc.convert(content, 'rst', format='html')

        lines = content.splitlines()
        lines.insert(2, BLOG_HEADER % (date, slug))
        content = '\n'.join(lines)

        content = fix_images(content)

        # print(content)
        filename = POSTS_DIR / slug
        with open(str(filename) + '.rst', 'wt') as f:
            f.write(content)
    # print(soup.prettify())


if __name__ == '__main__':
    bsoup()
