"""blogsite URL Configuration

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
'''
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/',admin.site.urls),
    path('myblog/',include('myblog.urls')),
    path('comments/',include('django_comments.urls'))
]
'''
from django.urls import path,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from myblog import views as myblog_views
from myblog.feed import LatestEntriesFeed
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from myblog.models import Entry

info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'modifyed_time'
}



urlpatterns = [
    path('admin/', admin.site.urls),
    path('myblog/',include('myblog.urls',namespace='myblog')),
    path('comments/',include('django_comments.urls')),
    path('latest/feed/', LatestEntriesFeed()),    #RSS订阅
    path('sitemap\.xml', sitemap, {'sitemaps': {'myblog': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),       #站点地图
    path('login/', myblog_views.login),
    path('register/',myblog_views.register),
    path('logout/', myblog_views.logout),
    path('captcha', include('captcha.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

