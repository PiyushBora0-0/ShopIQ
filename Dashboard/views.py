from django.shortcuts import render,HttpResponse

# Create your views here.

def dashboard(request):
    return render(request,'index.html')

def Analytics(request):
    return render(request,'Analytics.html')

def Addentry(request):
    return render(request,'AddEntry.html')