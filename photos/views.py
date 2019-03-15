from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
#..........
import datetime as dt

# Create your views here.
def welcome(request):
     images = Image.get_images()
    return render(request, 'welcome.html')

def photos_of_day(request):
    date = dt.date.today()
    return render(request, 'all-photos/today-photos.html', {"date": date,})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day    

def past_days_photos(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_of_day)

    return render(request, 'all-photos/past-photos.html', {"date": date ,"photos":photos})
def search_image(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = image.search_by_image(category)
        message = f"{category}"

        return render(request, 'all-photos/search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message}) 
def image(request,image_id):
    try:
       iamge = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image":image})           
def filter_by_location(request,location_id):
    """
    Function that filters images by location
    """
    images = Image.filter_by_location(id= location_id)
    return render (request, 'location.html', {"images":images})    