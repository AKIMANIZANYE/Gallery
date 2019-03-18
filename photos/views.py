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

    if 'Image' in request.GET and request.GET["Image"]:
        search_term = request.GET.get("Image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
