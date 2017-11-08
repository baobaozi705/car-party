# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404,get_list_or_404,render

# Create your views here.
from ../indexCarParty.models import Item,FirstType,SecondType
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def buy(request,item_name):
	i=get_object_or_404(Item,item_name=item_name)
	i.deitem1()
	render(request,'buyCarParty/buy.html',context)
	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

