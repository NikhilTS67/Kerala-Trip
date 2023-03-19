from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import TripForm
from .models import Trip

# Create your views here.

def index(request):
    trip=Trip.objects.all()
    context={'trip':trip}
    return render(request,'index.html', context)
def details(request,ID):
    trip=Trip.objects.get(id=ID)
    context={'details':trip}
    return render(request, 'details.html', context)
def add(request):
    if request.method=="POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        trip = Trip(name=name, desc=desc, img=img)
        trip.save()

    return render(request, 'add.html')
def edit(request,ID):
    trip = Trip.objects.get(id=ID)
    form = TripForm(request.POST or None, request.FILES, instance=trip)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form, 'trip': trip}
    return render(request, 'edit.html', context)
def delete(request, ID):
    if request.method=='POST':
        trip = Trip.objects.get(id=ID)
        trip.delete()
        return redirect('/')
    return render(request, 'delete.html')

