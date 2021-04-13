from django.shortcuts import render
from .models import *

# Create your views here.
def homepageView(request):
    return render(request, 'index.html')

def roomView(request):
    room_no = request.POST['room_no']
    name = request.POST['name']
    messages = []
    try:
        for eachobj in ChatModel.objects.filter(room_no=room_no).all():
            messages.append(eachobj.message)
            
    except Exception as e:
        print(e)

    return render(request, 'room.html', {'room_no': room_no, 'name': name, 'messages': messages})
