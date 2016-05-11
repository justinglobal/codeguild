"""jokes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from . import views

urlpatterns = [
    url(r'^jokes/test', views.render_page),
    url(r'^jokes/form/', views.render_form_page, name='form_page'),
    url(r'^jokes/submit/', views.render_ack, name='submit'),
    url(r'^jokes/index/' , views.render_index, name='index')
]

# url(r'^$', views.render_index, name='index'),
# url(r'^form/$', views.render_form, name='form_page'),
# url(r'^form/submit$', views.render_ack),
