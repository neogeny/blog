AUTHOR = 'Apalala'
SITENAME = 'Neogeny'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/Caracas'
DEFAULT_LANG = 'en'

RELATIVE_URLS = True

IGNORE_FILES = ['content/kaput', 'kaput']

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

OUTPUT_PATH = 'build/html/'
DEFAULT_PAGINATION = False

THEME = "themes/brownstone"
