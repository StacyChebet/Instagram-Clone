from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .forms import postImage
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,User

# Create your views here.

def login(request):
    return render(request, 'registration/login.html')


@login_required(login_url='/accounts/login')
def index(request):
    images = Image.objects.all()
    print(images)
    return render(request, 'index.html', {"images":images})
     

def profile(request):
    images = Image.objects.filter(poster_id = request.user.id)
    return render(request, 'profile.html', {"profile":profile, "images":images})

@login_required(login_url = '/accounts/login/')
def new_post(request):
    current_user = request.user 
    if request.method == 'POST':
        form = postImage(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.poster = current_user
            image.save()
        return redirect('index')

    else:
        form = postImage()
    return render(request, 'new_post.html', {"form":form})

@login_required(login_url = '/accounts/login/')
def search_results(request):
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = User.search_by_username(search_term)
        message = f"{search_term}"
        
        return render(request, 'search_results.html', {"message": message, "users": searched_users})

    else:
        message = "You haven't searched for any user"
        return render(request, 'search_results.html', {"message": message})


