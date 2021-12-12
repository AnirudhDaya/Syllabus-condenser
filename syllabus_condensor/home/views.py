from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import *


# Create your views here.
def index(request):
    if request.method == 'POST':

        form1 = UploadQuestions(request.POST,request.FILES)
        form2 = UploadQuestions(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return HttpResponse('The file is saved')
    else:
        form1 = UploadQuestions()
        form2 = UploadQuestions()
        context = {
            'form1':form1,
            'form2':form2,
        }
    return render(request,'index.html',context)