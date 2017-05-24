"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render
from instructors.views import hello,hello_python,http,contact,sum_two,student_list,instructors_list



urlpatterns = [
    url(r'^$', hello),
    url(r'^http$', http),
    url(r'^contact/$', contact),   
    url(r'^student_list/$', student_list),   
    url(r'^instructors/$', instructors_list),
    url(r'^python/(?P<some>\w+)/$', hello_python),

    url(r'^sum/(?P<a>\d+)/(?P<b>\d+)/$', sum_two),
    url(r'^admin/', admin.site.urls),
]
