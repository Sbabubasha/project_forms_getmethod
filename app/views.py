from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def form(request):
    if request.method=='POST':
        user=request.POST['user']
        pw=request.POST['pw']
        return HttpResponse('form add successfull')
    return render(request,'get.html')