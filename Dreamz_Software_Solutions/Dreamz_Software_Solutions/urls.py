"""Dreamz_Software_Solutions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from user_records import views
urlpatterns = [
    path('landing-page',views.landingPage),
    path('sign-up',views.signUp),
    path('login',views.Login),
    path('user-list',views.List_Of_User),
    path('<int:id>/',views.show_records_and_edit,name="editdata"),
    path('admin/', admin.site.urls),
]