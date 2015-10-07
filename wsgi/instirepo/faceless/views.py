from ctypes import c_short
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.shortcuts import render, redirect
from PIL import Image
from django.template import RequestContext
from django.template.context_processors import request
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.core import serializers
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from faceless.models import *
from django.core import serializers
from push_notifications.models import GCMDevice


@csrf_exempt
def signup_request(request):
    team_name_req = request.POST.get('team_name')
    username_req = request.POST.get('username')
    password_req = request.POST.get('password')

    user_profile_id = None
    error = True

    try:
        query = Teams.objects.get(name=team_name_req)
    except:
        team = Teams(name=team_name_req)
        team.save()

        username = username_req + "@" + team_name_req
        user = User.objects.create_user(username, username, password_req)
        user.first_name = username_req
        user.last_name = team_name_req
        user.save()

        user_profile = UserProfiles(user_link_obj=user, team_id=team, is_admin=True, is_first_time_login=False)
        user_profile.save()
        user_profile_id = user_profile.id

        error = False

    return JsonResponse({'error': error, 'id': user_profile_id, 'is_admin': True})


@csrf_exempt
def check_team_exist(request):
    team_name_req = request.POST.get('team_name')

    exist = None
    try:
        query = Teams.objects.get(name=team_name_req)
        exist = True
    except:
        exist = False

    return JsonResponse({'exist': exist})


@csrf_exempt
def login_request(request):
    team_name_req = request.POST.get('team_name')
    username_req = request.POST.get('username')
    password_req = request.POST.get('password')

    error = True
    password_change_required = False
    user_profile_id = None

    username = username_req + "@" + team_name_req
    user = authenticate(username=username, password=password_req)
    if user is not None:
        user_profile = user.user_profile
        if user_profile.is_first_time_login:
            password_change_required = True
            user_profile.is_first_time_login = False
            user_profile.save()
        user_profile_id = user_profile.id
        error = False

    return JsonResponse({'error': error, 'password_change_required': password_change_required, 'id': user_profile_id})


@csrf_exempt
def add_user_to_team(request):
    username_req = request.POST.get('username')
    password_req = request.POST.get('password')
    user_profile_id_req = request.POST.get('user_profile_id')

    error = True

    user_profile = UserProfiles.objects.get(pk=int(user_profile_id_req))
    if user_profile.is_admin:
        username = username_req + "@" + user_profile.team_id.name
        try:
            query = User.objects.get(username=username)
        except:
            user = User.objects.create_user(username, username, password_req)
            user.first_name = username_req
            user.last_name = user_profile.team_id.name
            user.save()

            user_profile = UserProfiles(user_link_obj=user, team_id=user_profile.team_id)
            user_profile.save()
            error = False

    return JsonResponse({'error': error})


@csrf_exempt
def add_gcm_token(request):
    gcm_token = request.POST.get('gcm_token')
    user_profile_id_req = request.POST.get('user_profile_id')
    device_id = request.POST.get('device_id')

    user_profile = UserProfiles.objects.get(pk=int(user_profile_id_req))

    created_new = True
    try:
        gcm_model = GCMDevice.objects.get(user=user_profile.user_link_obj)
        gcm_model.registration_id = gcm_token
        gcm_model.active = True
        gcm_model.save()
        created_new = False
    except:
        gcm_device_model = GCMDevice(name=user_profile.user_link_obj.username, user=user_profile.user_link_obj,
                                     device_id=device_id, registration_id=gcm_token)
        gcm_device_model.save()

    return JsonResponse({'created_new': created_new})


@csrf_exempt
def make_channel(request):
    channel_name = request.POST.get('channel_name')
    user_profle_id = request.POST.get('user_profile_id')

    error = True

    user_profile = UserProfiles.objects.get(pk=int(user_profle_id))
    if user_profile.is_admin:
        try:
            query = Channels.objects.get(name=channel_name, company_id=user_profile.team_id)
        except:
            channel_model = Channels(name=channel_name, company_id=user_profile.team_id)
            channel_model.save()
            error = False

    return JsonResponse({'error': error})