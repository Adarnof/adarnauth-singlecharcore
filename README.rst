=====
Adarnauth-SingleCharCore
=====

Adarnauth-SingleCharCore is a Django app for managing users as they relate to a single character in EVE Online.

Quick start
-----------
1. Add "singlecharcore" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'singlecharcore',
    ]

2. Include the singlecharcore URLconf in your project urls.py like this::

    url(r'^core/', include('singlecharcore.urls')),

3. Set your project's user model to singlecharcore.User in settings.py::

    AUTH_USER_MODEL = 'singlecharcore.User'
    AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',
        'singlecharcore.backends.TokenAuthenticationBackend',
    ]
    LOGIN_URL = 'singlecharcore:login'

4. Optionally configure additional settings::

    LOGIN_REDIRECT_URL = 'my_app:view'
    LOGOUT_REDIRECT_URL = 'my_app:public_view'
    ACCOUNT_INACTIVE_MESSAGE = '<h1>Your account is not active. Please contact an admin.</h1>'
    LOGIN_SCOPES = ['myScope']

5. Run python manage.py migrate to create the singlecharcore models.
