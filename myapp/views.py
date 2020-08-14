from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def base(request):
    return render(request,"base.html")
def profile(request):
    name='ASHOK'
    return render(request,"myapp/profile.html",{'name':name})
def home(request):
    return render(request,"myapp/home.html")
def register(request):
    if request.method=="POST":
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        password= request.POST.get('password')
        date= request.POST.get('date')
        send_mail('thanks for registration','mr./ms.{} {}'.format(first_name, last_name),'ashokbuengg@gmail.com',[email,],fail_silently=True)
        #return HttpResponse('<h1>{}<br>{}<br>{}<br>{}<br>{}</h1>'.format(first_name, last_name, email, password, date))
        return redirect("home")
    return render(request,"registration.html")

from django.core.files.storage import FileSystemStorage
def img_upld(request):
    return render(request,'img_upld.html')

from myapp.utilities import store_image
def img_disp(request):
    file_urls=False
    if request.method=="POST" and request.FILES:
        image1=request.FILES.get('img1')
        image2=request.FILES.get('img2')
        file_urls=map(store_image,[image1,image2])
    return render(request,"img_disp.html",context={'file_urls':file_urls})