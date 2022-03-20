"""Food_system URL Configuration

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

from django.contrib import admin
from django.urls import path , include
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
#for static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    path('admin/', admin.site.urls),
     path('project/' , include('project.urls')),
    path('profile/' , accounts_views.profile , name='profile'),
    path('register/' ,accounts_views.register , name='register'),
    path('Agent_login/' , accounts_views.Agent_login , name="Agent"),
    path('Donate/' , accounts_views.Donate , name="Donate"),
    path('Donate_food/' , accounts_views.Donate_food , name="Donate_food"),
    path('status/' , accounts_views.status , name="status"),
    path('feedback/' , accounts_views.feedback , name="feedback"),
    path('Feedback/' , accounts_views.Feedback , name="Feedback"),
    path('Agent_status/' , accounts_views.Agent_status , name="Agent_status"),
    path('login/' ,auth_views.LoginView.as_view(template_name='project/base.html') , name='login'),
    path('logout/' ,auth_views.LogoutView.as_view(template_name='accounts/logout.html') , name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
