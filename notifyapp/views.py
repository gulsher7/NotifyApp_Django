from django.shortcuts import render
from .models import *

def index(request):
    data = Post.objects.all().order_by('-id')
    return render(request, 'notifyapp/index.html', {'data':data})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        databs = Contact(user_name=name, user_email=email, user_phone=phone, user_desc=desc)
        databs.save()
    return render(request, 'notifyapp/contact.html')
    
