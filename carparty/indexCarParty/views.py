# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404,get_list_or_404,render

# Create your views here.
from django.http import HttpResponse
# from django.template import loader
from .models import Item,FirstType,SecondType
import os
from django.http import Http404
from django.views import generic

def index(request):
	ft=FirstType.objects.all()
	st=SecondType.objects.all()
	# template=loader.get_template('indexCarParty/index.html')
	context={
	'ft':ft,
	'st':st,
	}
	# foutput=' '.join([f.ft_name for f in ft])
	# soutput=os.linesep+' '.join([s.st_name for s in st])
	return render(request,'indexCarParty/index.html',context)

class IndexView(generic.ListView):
	template_name='indexCarParty/index.html'
	context_object_name='index'
		
		

def st(request,ft_name):
	f=FirstType.objects.get(ft_name=ft_name)
	# try:
	# 	st=SecondType.objects.filter(st_ft=f)
	# except SecondType.DoesNotExist:
	# 	raise Http404("dose not exist of your search!")
	st=get_list_or_404(SecondType,st_ft=f)
	# fid=FirstType.objects.filter(ft_name=ft_name)
	# st=SecondType.objects.filter(st_ft=fid)
	# stoutput=' '.join([s.st_name for s in st])
	# allitem=[]
	# for s in st:
	# 	it=Item.objects.filter(item_subtype=s)
	# 	allitem+=it
	# f=f[0]
	context={
	'f':f,
	'st':st,
	}
	return render(request,'indexCarParty/st.html',context)

def item(request,ft_name,st_name):
	# fid=FirstType.objects.filter(ft_name=ft_name)
	# st=SecondType.objects.filter(st_ft=fid)
	
	sid=SecondType.objects.filter(st_name=st_name)
	it=Item.objects.filter(item_subtype=sid)
	ioutput=' '.join([i.item_name for i in it])
	return HttpResponse(ioutput)