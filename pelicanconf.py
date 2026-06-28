AUTHOR = 'Apalala'
SITENAME = 'Neogeny'
SITEURL = 'https://neogeny.github.io/blog'

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

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

SOCIAL = ()

OUTPUT_PATH = 'build/html/'
DEFAULT_PAGINATION = False

THEME = "themes/brownstone"
