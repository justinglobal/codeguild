"""flutter URL Configuration

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
    url(r'^admin/', admin.site.urls),
    url(r'^flut/index$', views.render_index, name='index'),
    url(r'^post$', views.render_post_page, name='post_page'),
    url(r'^post/submit$', views.render_post_ack, name='post_ack')
]

  # url(r'^add$', views.render_add_playlist, name='add_playlist'),
  # url(r'^add/submit$', views.render_add_playlist_ack, name='add_playlist_submit'),
