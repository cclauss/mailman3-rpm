# Mailman Web configuration file.
# /etc/mailman3/settings.py

# Get the default settings from mailman_web/settings/mailman.py
from mailman_web.settings.base import *
from mailman_web.settings.mailman import *

# Settings below supplement or override the defaults.
# see also https://docs.djangoproject.com/en/4.1/ref/settings/

#: Default list of admins who receive the emails from error logging.
ADMINS = [
        # ('Mailman Suite Admin', 'root@localhost'), # optional for sending exceptions via e-mail
]

# Postgresql database setup.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/@VARDIR@/db/mailman.db',
    }
}

# 'collectstatic' command will copy all the static files here.
# Alias this location from your webserver to `/static`
STATIC_ROOT = '@VARDIR@/web/static'

# enable the 'compress' command.
COMPRESS_ENABLED = True

# Make sure that this directory is created or Django will fail on start.
LOGGING['handlers']['file']['filename'] = '@LOGDIR@/mailmanweb.log'

#: See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    "localhost",  # Archiving API from Mailman, keep it.
    "127.0.0.1",
    # "lists.your-domain.org",
    # Add here all production domains you have.
]

#: See https://docs.djangoproject.com/en/dev/ref/settings/#csrf-trusted-origins
#: these are of the form 'https://lists.example.com' or
#: 'https://*.example.com' to include subdomains
CSRF_TRUSTED_ORIGINS = [
    # "https://lists.your-domain.org",
    # Add here all production domains you have.
]

#: Current Django Site being served. This is used to customize the web host
#: being used to serve the current website. For more details about Django
#: site, see: https://docs.djangoproject.com/en/dev/ref/contrib/sites/
SITE_ID = 1

# Set this to a new secret value.
SECRET_KEY = '@SECRET_KEY@'

# Set this to match the api_key setting in
# /opt/mailman/mm/mailman-hyperkitty.cfg (quoted here, not there).
MAILMAN_ARCHIVER_KEY = '@MAILMAN_ARCHIVER_KEY@'

# default with custom PATH
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': "@VARDIR@/archives/haystack/fulltext_index",
    },
}

# The sender of emails from Django such as address confirmation requests.
# Set this to a valid email address.
DEFAULT_FROM_EMAIL = 'admin@example.com'

# The sender of error messages from Django. Set this to a valid email
# address.
SERVER_EMAIL = 'admin@example.com'


# see also
# https://docs.mailman3.org/en/latest/config-web.html
# https://docs.mailman3.org/projects/mailman-web/en/latest/settings.html
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
# EMAIL_HOST_USER = <username>     # optional
# EMAIL_HOST_PASSWORD = <password> # optional

# Mailman Core default API Path
MAILMAN_REST_API_URL = 'http://localhost:@RESTAPIPORT@'
MAILMAN_REST_API_USER = 'restadmin'
MAILMAN_REST_API_PASS = '@RESTAPIPASS@'

# Postorius
POSTORIUS_TEMPLATE_BASE_URL = 'http://localhost:@WEBPORT@'


### CAPTCHA support

## Google
# service   : https://developers.google.com/recaptcha
# django-app: https://pypi.org/project/django-recaptcha/
INSTALLED_APPS.append('captcha')
RECAPTCHA_PUBLIC_KEY  = '<your sitekey>'
RECAPTCHA_PRIVATE_KEY = '<your secret key>'
RECAPTCHA_DOMAIN      = 'www.recaptcha.net'
# RECAPTCHA_PROXY       = {'http': 'http://127.0.0.1:3128', 'https': 'https://127.0.0.1:3128'} # optional

## hCaptcha
# general   : https://docs.hcaptcha.com/
# django-app: https://pypi.org/project/django-hCaptcha/
INSTALLED_APPS.append('hcaptcha')
HCAPTCHA_SITEKEY = '<your sitekey>'
HCAPTCHA_SECRET  = '<your secret key>'
# HCAPTCHA_PROXIES = {'http': 'http://127.0.0.1:3128', 'https': 'https://127.0.0.1:3128'} # optional

## FriendlyCaptcha
# service   : https://docs.friendlycaptcha.com/
# django-app: https://pypi.org/project/django-friendly-captcha/
INSTALLED_APPS.append('friendly_captcha')
FRC_CAPTCHA_SITE_KEY         = '<your sitekey>'
FRC_CAPTCHA_SECRET           = '<your secret key>'
FRC_CAPTCHA_VERIFICATION_URL = 'https://api.friendlycaptcha.com/api/v1/siteverify'

## CAPTCHA selector
# CAPTCHA_SERVICE = 'recaptcha'
# CAPTCHA_SERVICE = 'hcaptcha'
# CAPTCHA_SERVICE = 'friendlycaptcha'


# Disable gravatar by default
HYPERKITTY_ENABLE_GRAVATAR = False
INSTALLED_APPS.remove('django_gravatar')
