from django.shortcuts import render

def Index (request):
    return render(request ,'pages/Index.html')
def About (request):
    return render(request ,'pages/About.html')
def Shipping (request):
    return render(request,'pages/Shipping.html')
def Tracking (request):
    return render(request,'pages/Tracking.html')
def Support (request):
    return render(request,'pages/Support.html')
def signIn (request):
    return render(request,'pages/signIn.html')
def SignUp (request):
    return render(request,'pages/SignUp.html')
def SignUpB (request):
    return render(request,'pages/SignUpB.html')
