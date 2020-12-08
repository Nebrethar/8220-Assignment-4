"""assign4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

from assign4 import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),
    path('roleSU.html', views.roleSU, name='roleSU'),
    path('roleLI.html', views.roleLI, name='roleLI'),
    path('loginform.html', views.loginform, name='loginform'),
    url('userlogin', views.userlogin, name='userlogin'),
    url('signupPE', core_views.signupPE, name='signupPE'),
    url('signupHM', core_views.signupHM, name='signupHM'),
    url('homepageHM', core_views.homepageHM, name='homepageHM'),
    url('homepagePE', core_views.homepagePE, name='homepagePE'),
    #url('accounts/login/$', auth_views.LoginView.as_view(template='login.html'), name='login'),
    #url('accounts/logout/$', auth_views.LogoutView, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)