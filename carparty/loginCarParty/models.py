# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from ../indexCarParty.models import Item
class User(models.Model):
	user_mnumber=model.IntegerField(max_length=11,unique=True)
	user_name=model.CharField(max_length=120,unique=True)
	user_psw=model.CharField(max_length=16)
	user_gender=model.BooleanField(blank=True)
	user_age=model.IntegerField(max_length=3,blank=True)
	user_intro=model.TextField(max_length=120,blank=True)
	user_create=model.DateField(auto_now_add=True)
class sc(models.Model):
	sc_name=model.ForeignKey(Item,on_delete=models.CASCADE)
	sc_user=model.ForeignKey(User,on_delete=models.CASCADE)
	sc_dt=model.DateTimeField(auto_now_add=True)
class mg(models.Model):
	mg_name=model.ForeignKey(Item,on_delete=models.CASCADE)
	mg_user=model.ForeignKey(User,on_delete=models.CASCADE)
	mg_dt=model.DateTimeField(auto_now_add=True)
