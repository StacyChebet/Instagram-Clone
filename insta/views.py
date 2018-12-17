from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Image,Profile
import datetime as dt
from .forms import postImage
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

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