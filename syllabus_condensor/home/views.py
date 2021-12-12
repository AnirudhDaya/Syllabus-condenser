from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import *
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import nltk
from nltk.corpus import stopwords
import subprocess
from django.views.generic.edit import FormView

class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
# Create your views here.
def index(request):
    if request.method == 'POST':
        file1 = FileFieldForm(request.POST,request.FILES)

        if file1.is_valid():
            file1.save()

            return HttpResponse("Success..!!")

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
    return render(request,'index.html')
