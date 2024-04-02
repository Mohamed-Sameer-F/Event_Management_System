from django.shortcuts import redirect, render

from eventapp.forms import BookingForm

from . models import Event

# Create your views here.

def index(request):
    return render(request,'index.html')

def event(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request,'event.html',dict_eve)

def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)
