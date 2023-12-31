"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='django-insecure-$o78(-d@o%z-l2@z23p9#rpaf+ykvu8j8=j6g0k%v+wg$ob(l&')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'tinymce',
    'base',
    'web',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'web.context_processors.context',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('DATABASE_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': env('DATABASE_NAME', default='db.sqlite3'),
        'USER': env('DATABASE_USER', default=''),
        'PASSWORD': env('DATABASE_PASSWORD', default=''),
        'HOST': env('DATABASE_HOST', default='localhost'),
        'PORT': env('DATABASE_PORT', default=''),
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = env.str('LANGUAGE_CODE', default='en-us')

TIME_ZONE = env.str('TIME_ZONE', default='UTC')

USE_I18N = env.bool('USE_I18N', default=True)

USE_TZ = env.bool('USE_TZ', default=True)

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]


USE_THOUSAND_SEPARATOR = env.bool('USE_THOUSAND_SEPARATOR', default=True)

THOUSAND_SEPARATOR = env.str('THOUSAND_SEPARATOR', default=',')

NUMBER_GROUPING = env.int('NUMBER_GROUPING', default=3)

DECIMAL_SEPARATOR = env.str('DECIMAL_SEPARATOR', default='.')


DATE_FORMAT = env.str('DATE_FORMAT', default=None)

DATETIME_FORMAT = env.str('DATETIME_FORMAT', default=None)

SHORT_DATETIME_FORMAT = env.str('SHORT_DATETIME_FORMAT', default=DATETIME_FORMAT)

FIRST_DAY_OF_WEEK = env.int('FIRST_DAY_OF_WEEK', default=1)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = env('STATIC_URL', default='static/')

STATIC_ROOT = env('STATIC_ROOT', default=(BASE_DIR / 'staticfiles'))

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'npm.finders.NpmFinder',
]

MEDIA_URL = env('MEDIA_URL', default='media/')

MEDIA_ROOT = env('MEDIA_ROOT', default=(BASE_DIR / 'media'))


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = env.int('SITE_ID', default=1)


# User

AUTH_USER_MODEL = 'base.User'

LOGIN_URL = env.str('LOGIN_URL', default='account_login')

LOGIN_REDIRECT_URL = env.str('LOGIN_REDIRECT_URL', default='/')

AUTHENTICATION_METHOD = 'email'

AUTHENTICATION_CLASSES = [
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Session

SESSION_EXPIRE_AT_BROWSER_CLOSE = env.bool('SESSION_EXPIRE_AT_BROWSER_CLOSE', default=False)

SESSION_COOKIE_AGE = env.int('SESSION_COOKIE_AGE', default=315360000)


# Data upload

DATA_UPLOAD_MAX_MEMORY_SIZE = env.int('DATA_UPLOAD_MAX_MEMORY_SIZE', default=15728640)

DATA_UPLOAD_MAX_NUMBER_FIELDS = env.int('DATA_UPLOAD_MAX_NUMBER_FIELDS', default=20480)


# X-Frame Options

X_FRAME_OPTIONS = env.str('X_FRAME_OPTIONS', 'SAMEORIGIN')

XS_SHARING_ALLOWED_METHODS = env.list('XS_SHARING_ALLOWED_METHODS', default=['POST','GET','OPTIONS', 'PUT', 'DELETE'])


# Email

EMAIL_BACKEND = env.str('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

EMAIL_USE_SSL = env.bool('EMAIL_USE_SSL', default=False)

EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=False)

EMAIL_PORT = env.int('EMAIL_PORT', default=587)

EMAIL_HOST = env.str('EMAIL_HOST', default=None)

EMAIL_HOST_USER = env.str('EMAIL_HOST_USER', default=None)

EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD', default=None)


# Rest Framework

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': env.list('REST_FRAMEWORK_DEFAULT_RENDERER_CLASSES', default=[
        'rest_framework.renderers.JSONRenderer',
    ]),
}


# Tinymce settings.py

TINYMCE_DEFAULT_CONFIG = {
    'height': env.int('TINYMCE_HEIGHT', default=360),
    'width': env.int('TINYMCE_WIDTH', default=800),
    'plugins': env.str('TINYMCE_PLUGINS', default='advlist autolink lists link image charmap print preview hr anchor pagebreak code'),
    'toolbar': env.str('TINYMCE_TOOLBAR', default='undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | code'),
    'extended_valid_elements': env.str('', default='iframe[src|width|height|name|align|frameborder|scrolling]'),
}
