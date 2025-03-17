AUTHOR = 'Shashwat Pathak'
SITENAME = 'AI, Python and Blackjack'
SITEURL = ""

PATH = "content"
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
DEFAULT_PAGINATION = True
# THEME = "../pelican-themes/blue-penguin-dark"
ARTICLE_EXCLUDES = ['pages']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
# )

# Social widget
SOCIAL = (
    ("Linkedin", "https://linkedin.com/in/shashwatpathak"),
)

# DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MENUITEMS = (
  ('Home', '/'),
  ('About me', '/pages/about-me/index.html'),
  ('AI', '/category/ai/index.html'),
  ('Blackjack', '/category/blackjack/index.html'),
  ('Python', '/category/python/index.html'),
)
