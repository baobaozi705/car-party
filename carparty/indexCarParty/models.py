# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FirstType(models.Model):
	ft_name=models.CharField(max_length=120)
	def __unicode__(self):
		return self.ft_name

class SecondType(models.Model):
	st_name=models.CharField(max_length=120)
	st_ft=models.ForeignKey(FirstType,on_delete=models.CASCADE)
	def __unicode__(self):
		return self.st_name

class Item(models.Model):
	item_name=models.CharField(max_length=120)
	item_price=models.DecimalField(max_digits=10,decimal_places=2)
	item_match=models.CharField(max_length=200)
	item_brand=models.CharField(max_length=120)
	item_time=models.DateTimeField(auto_now=True)
	item_num=models.IntegerField()
	item_type=models.ForeignKey(FirstType,on_delete=models.CASCADE)
	item_subtype=models.ForeignKey(SecondType,on_delete=models.CASCADE)
	def deitem1(self):
		item_num-=1
		self.save()
	def __unicode__(self):
		return self.item_name