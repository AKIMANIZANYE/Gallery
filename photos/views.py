from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
#..........
import datetime as dt
from .models import Image

# Create your views here.

def photos_of_day(request):
    date = dt.date.today()
    photos = Image.objects.all()

    return render(request, 'photos_of_day.html', {"date": date,"images":photos})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"/image.html", {"image":image})


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_input = request.GET.get("image")
        searched_images = Image.search_by_category(search_input)
        # print(searched_images)
        message = f"{search_input}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
def display_images_categories(request):    
   photos = Image.category(1)
   return render(request, 'category.html', {"photos":photos}) 

def display_images_locations(request):    
   photos = Image.location(2)
   return render(request, 'location.html', {"photos":photos})        
