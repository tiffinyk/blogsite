'''
from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name = 'index'),
    path('home', views.home),
    path('detail',views.detail)
]
'''
from django.urls import path
from . import views


app_name = 'myblog'


urlpatterns = [
    path('index', views.index,name='index'),
    path('detail/<entry_id>/', views.detail,name='detail'),
    path('category/(p<category_id>[0-9]+)/', views.catagory,name='myblog_category'),
    path('tag/(p<tag_id>[0-9]+)/',views.tag,name='myblog_tag'),
    path('search/', views.search,name='myblog_search'),
    path('reply/(P<comment_id>\d+)/', views.reply, name='comment_reply'),
    path('archives/(P<year>[0-9]+)/(P<month>[0-9]+/)', views.archives, name='myblog_archives'),

]