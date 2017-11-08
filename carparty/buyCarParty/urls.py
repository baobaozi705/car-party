from django.conf.urls import url,include

from . import views

app_name='buyCarParty'

urlpatterns=[url(r'^$',views.buy,name='buy'),	
				]