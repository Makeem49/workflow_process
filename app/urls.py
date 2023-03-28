"""app URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('process/', include('process.urls')),
    path('process/<str:process_name>/stages/', include('stages.urls')),
    path('process/<str:process_name>/stage/<str:stage_name>/steps/', include('steps.urls')),
    path('grant/', include('grant_access.urls')),
    path('<str:process_name>/<str:stage_name>/<str:step_name>/create', include('actions.urls'))
]