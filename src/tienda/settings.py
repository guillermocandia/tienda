import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LOCAL = False
DEBUG = TRUE
TEMPLATE_DEBUG = False

DEFAULT_CHARSET = 'utf-8'

SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
SESSION_COOKIE_AGE = 86400
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# ALLOWED_HOSTS = ['']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'polymorphic',
    'adminsortable',
    'app',
    'solie.payments',
    'solie.util',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'storages',
    'mathfilters',
    'corsheaders',
    'django_summernote'
    
    #'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
    'app.processors.category_list_proc',
    'solie.util.processors.aviso_proc'
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)

SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGOUT_ON_GET = True

ROOT_URLCONF = 'tienda.urls'
WSGI_APPLICATION = 'tienda.wsgi.application'

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True

EMAIL_FROM = 'Ventas <ventas@ejemplo.com>'
EMAIL_ADMIN = ''
if LOCAL:
    EMAIL_NOTIFY = ['']
else:
    EMAIL_NOTIFY = ['Ventas <ventas@ejemplo.com>']

if LOCAL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
    
    STATIC_ROOT = '/home/trabajos/0000013/app/tienda_static/static'
    STATIC_URL = 'http://static.dev.ejemplo.com/static/'
    MEDIA_ROOT = '/home/trabajos/0000013/app/tienda_static/media'
    MEDIA_URL = 'http://static.dev.ejemplo.com/media/'
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'tienda',
            'USER': 'tienda',
            'PASSWORD': '',
            'HOST': 'com-ejemplo.c53ly7mvediv.us-west-1.rds.amazonaws.com',
            'PORT': '3306',
        }
    }
  
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_S3_SECURE_URLS = False
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_ACCESS_KEY_ID = ''
    AWS_S3_SECRET_ACCESS_KEY = ''
    AWS_STORAGE_BUCKET_NAME = 'com-ejemplo-static'

    AWS_S3_URL_PROTOCOL = 'http:'
    AWS_S3_CUSTOM_DOMAIN = 'static.ejemplo.com'
    #AWS_S3_CUSTOM_DOMAIN = 'com-ejemplo-static.s3-us-west-1.amazonaws.com'
    
    STATIC_ROOT = '/home/trabajos/0000013/app/tienda_ejemplo_static/static'
    STATIC_URL = 'http://static.ejemplo.com/'
    #STATIC_URL = 'http://com-ejemplo-static.s3-us-west-1.amazonaws.com/'
CORS_ALLOW_CREDENTIALS = True
if DEBUG:
    KHIPU_RECEIVER_ID = ''
    KHIPU_SECRET = ''
    
else:
    KHIPU_RECEIVER_ID = ''
    KHIPU_SECRET = ''
    
if LOCAL:
    WEBPAY_TMP = '/tmp/'
    WEBPAY_CGI_CHECK_MAC = '/home/trabajos/0000013/app/cgi-bin/tbk_check_mac.cgi'
    TBK_URL_EXITO = 'http://app.dev.ejemplo.com/payments/webpay/success/'
    TBK_URL_FRACASO = 'http://app.dev.ejemplo.com/payments/webpay/error/'
    URL_CGI = 'http://app.dev.ejemplo.com/cgi-bin/tbk_bp_pago.cgi'
else: 
    WEBPAY_TMP = '/tmp/'
    WEBPAY_CGI_CHECK_MAC = '/var/www/cgi-bin/tbk_check_mac.cgi'
    TBK_URL_EXITO = 'http://app.ejemplo.com/app/payments/webpay/success/'
    TBK_URL_FRACASO = 'http://app.ejemplo.com/app/payments/webpay/error/'
    URL_CGI = 'http://app.ejemplo.com/cgi-bin/tbk_bp_pago.cgi'

if DEBUG:
    CSRF_COOKIE_DOMAIN = 'localhost'
    CORS_ORIGIN_ALLOW_ALL = False
    CORS_ORIGIN_WHITELIST = (
        'localhost',
    )
else:
    CSRF_COOKIE_DOMAIN = '.ejemplo.com'
    CORS_ORIGIN_ALLOW_ALL = False
    CORS_ORIGIN_WHITELIST = (
        'ejemplo.com',
        'www.ejemplo.com',
        'www2.ejemplo.com'
    )
