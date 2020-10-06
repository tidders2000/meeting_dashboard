"""screenpop URL Configuration

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

from django.urls import path, include
from .views import *


urlpatterns = [
    path('finance/', finance, name='finance'),
    path('hr/', hr, name='hr'),
    path('risklog/', risklog, name='risklog'),
    path('issues/', issues, name='issues'),
    path('actions/', actions, name='actions'),
    path('hr/<int:pk>', actions_ud, name='actud'),
    path('finance/<int:pk>', actions_ud, name='actud'),
    path('finance/issue/<int:pk>', issues_ud, name='issud'),
    path('hr/issue/<int:pk>', issues_ud, name='issud'),
    path('rag/', rag, name='rag'),
    path('charts/', charts, name='charts'),
    path('minutes/', minutes, name='minutes'),
    path('pdf/', pdf, name='pdf')





]
