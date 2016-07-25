from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from singlecharcore.app_settings import LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL, ACCOUNT_INACTIVE_MESSAGE, LOGIN_SCOPES
from eve_sso.decorators import token_required
from singlecharcore.models import User

@token_required(new=True, scopes=LOGIN_SCOPES)
def login_view(request, tokens):
    token = tokens[0]
    user = authenticate(token=token)
    if user.is_active:
        login(request, user)
        if not token.can_refresh:
            token.delete()
        next = request.GET.get('next', LOGIN_REDIRECT_URL)
        return redirect(next)
    return HttpResponseForbidden(ACCOUNT_INACTIVE_MESSAGE)

@login_required
def logout_view(request):
    logout(request)
    next = request.GET.get('next', LOGOUT_REDIRECT_URL)
    return redirect(next)
