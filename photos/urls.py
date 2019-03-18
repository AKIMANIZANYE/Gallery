from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns=[
  
     url('^$', views.photos_of_day, name='photos_of_day'),
     url(r'^image/(\d+)',views.image,name ='image'),
     url(r'^search/', views.search_results, name='search_results'),
     url(r'^category/', views.display_images_categories, name = 'category'),
     url(r'^location/', views.display_images_locations, name = 'location'),
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
