from django.conf.urls import url
from . import views

urlpatterns=[
  
    url('^$',views.photos_of_day,name='photosToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photos,name = 'pastphotos'),
    url(r'^search/', views.search_results, name='search_results')
] 
