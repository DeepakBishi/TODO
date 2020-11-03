"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url, include
# from accounts import views
from accounts import views
import myApp


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.loginView, name='login'),
    url(r'^signup/$', views.signupView, name='signup'),
    url(r'^logout/$', views.logoutView, name='logout'),
    url(r'^changepassword/(?P<email>[\w|\W.-]+)/$', views.changePasswordView, name='changepassword'),
    url(r'^account/', include('accounts.urls')),
    url(r'^todo/', include('myApp.urls')),
]
