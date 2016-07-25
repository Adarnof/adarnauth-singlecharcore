from django.conf import settings

LOGIN_REDIRECT_URL = getattr(settings, 'LOGIN_REDIRECT_URL', '/')
LOGOUT_REDIRECT_URL = getattr(settings, 'LOGOUT_REDIRECT_URL', '/')
ACCOUNT_INACTIVE_MESSAGE = getattr(settings, 'ACCOUNT_INACTIVE_MESSAGE', '<h1>User account disabled</h1>')
LOGIN_SCOPES = getattr(settings, 'LOGIN_SCOPES', [])
