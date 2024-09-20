AUTHOR = 'Shashwat Pathak'
SITENAME = 'AI, Python and Blackjack'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
# THEME = "../pelican-themes/blue-penguin-dark"
ARTICLE_EXCLUDES = ['pages']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
# )

# Social widget
SOCIAL = (
    ("Linkedin", "https://linkedin.com/in/shashwatpathak"),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MENUITEMS = (
  ('Home', '/'),
  ('About me', '/pages/about-me.html'),
  ('AI', '/category/ai.html'),
  ('Blackjack', '/category/blackjack.html'),
  ('Python', '/category/python.html'),
)
