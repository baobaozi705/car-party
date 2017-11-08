from django.conf.urls import url,include

from . import views

app_name='indexCarParty'

urlpatterns=[url(r'^$',views.index,name='index'),
			 url(r'^(?P<ft_name>[a-z]+\s?)/$',views.st,name='st'),
			 url(r'^(?P<ft_name>[a-z]+\s?)/(?P<st_name>[a-z]+\s?)/$',views.item,name='item'),
			 url(r'^buy/',include('buyCarParty.urls')),	
				]