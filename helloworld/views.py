from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import TextMessage

def index(request):

	t1 = TextMessage.objects.create(talker='Michael', message='Hello, Professor!')
	t2 = TextMessage.objects.create(talker='Pecu', message='Hello, Class!')
	t3 = TextMessage.objects.create(talker='Domi', message='Hello, Michael!')
	t1.save()
	t2.save()
	t3.save()

	msgs = TextMessage.objects.all()


	return render(request, 'guestbookver1.html', locals())