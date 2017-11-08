from django.conf.urls import url,include

from . import views

app_name='loginCarParty'

urlpatterns=[url(r'^$',views.login,name='login'),	