from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import TextMessage
import time

def guestbook(request):

	if request.method == 'POST':
		_talker = request.POST.get('name')
		if request.user.is_authenticated:
			_talker = request.user.username
		_message = request.POST.get('msg')
		_talktime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
		TextMessage.objects.create(talker=_talker, message=_message, talktime=_talktime)
		
	msgs = TextMessage.objects.all()

	return render(request, 'guestbookver1.html', locals())

def index(request):

	return render(request, 'index.html')