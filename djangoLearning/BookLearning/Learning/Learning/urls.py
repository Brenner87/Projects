"""Learning URL Configuration

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
from BookLearning import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^current_date/$', views.current_date),
    url(r'^time_offset/(-?\d{1,2})/$', views.time_offset),
    url(r'^best_time_offset/(-?\d{1,2})/$', views.best_time_offset),
    url(r'^newer_current_date/$', views.newer_current_date),
    url(r'^best_current_date/$', views.best_current_date),
    url(r'^get_service_info/$', views.get_service_info),
    url(r'^get_post/$', views.get_post),
    url(r'^test_search-form/$', views.test_search_form),
    url(r'^test_search/$', views.test_search),
    url(r'^search/$', views.search),
    #url(r'^search_results/$', views.search),
    url(r'^query_params/$', views.query_params),
    url(r'^contact/$', views.contact),
    url(r'^publishers/$', views.PublisherList.as_view()),
]
