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


def predictor():
    
    frequency = open('frequency.txt','w+')
    f = open('ocr.txt','w+')

    pages = convert_from_path('sample.pdf',500)             #convert pdf to pages 
    image_counter = 1
    for page in pages:                                      #loop to iterate through pages
        filename = "page_"+str(image_counter)+".jpg"
        page.save(filename,'JPEG')                          #saves the pages a jpg files
        image_counter +=1

    filelimit = image_counter-1                             #set file limit to one less than image counter


    custom_config = r'--oem 3 --psm 6'
    for i in range(1, filelimit + 1):                                       #loop to iterate through each image file of pages 
        filename = "page_"+str(i)+".jpg"
        text = str(pytesseract.image_to_string(Image.open(filename),config=custom_config))   #Convert image to text file
        # text = text.replace('-\n', '')                                      #Replace \n with '' 
        f.write(text)                                                       #Writes text to file 'f'

    f.seek(0)                                                               #Seeks file pointer to begining
    wh=['what','pages','who','explain','how','why','when','then','which','where','a','an','or','part','find','answer','and','the','0','1','2','3','4','5','6','7','8','9'] #List of unwanted words
    punctuations = ['(',')',';',':','[',']',',',"'"]
    freq = {}                                                                       #frequency dictionary initialized
    for line in f:                                                                  #Iterates through each line of text file
        for word in line.split():                                                   #Splits each line with space to aquire words
            if word not in stopwords.words('english') and word.lower()not in wh and word not in punctuations and word[-1]!=':':    #Checks words to exclude unwanted words
                word = word.lower()
                if word in freq:                                                    #Frequency of each word updated to dictionary
                    freq[word]+=1
                else:
                    freq[word]=1

    for w in sorted(freq, key=freq.get, reverse=True):                              #Loop to sort the dictionary
        w=w+"\n"                                                             
        frequency.write(w)                                                          #Writes to words to frequency in the sorted order



    pages_syl = convert_from_path('syllabus.pdf',500)                                   #Converts syllabus to pages
    image_counter_syl = 1           
    for page in pages_syl:                                                              #Iterates through each pages
        filename = "syllabus_"+str(image_counter_syl)+".jpg"                            
        page.save(filename,'JPEG')                                                  #Saves the file as jpg
        image_counter_syl +=1

    filelimit= image_counter_syl

    f1 = open('syllabus.txt','w+')                                                 #Opens the file syllabus.txt in appending,reading and writing mode
    for i in range(1, filelimit):
        filename = "syllabus_"+str(i)+".jpg"
        text = str(pytesseract.image_to_string(Image.open(filename),config=custom_config ))        #Convert image to text file
        # text = text.replace('-\n', '') 
        f1.write(text)                                                      
    f1.seek(0)
    f.seek(0)
    frequency.seek(0)

    flag=0
    i=0
    word_list=[]                                                                        #word_list list initialised 
    result = open('result.txt','a')                                                     #result text file opened in append mode
    for word in frequency:                                                              #Iterates through frequency.txt collecting each word
        for line in f1:                                                                 #Iterates through syllabus.txt collecting each line
            for w in line.split():                                                      #Splits line by " " and access words  
                if(word.lower()==w.lower() or word.lower()==w[0:-2].lower()):           #Checks if the word in both files are same
                    flag=1
                word_list.append(w)                                                     #Words appended to lsit 
                if(w[-1]==':'):                                                         #checks
                    word_list.clear()
                elif(w[-1] in [',',';']):
                    s = " "
                    str = s.join(word_list) + '\n'
                    result.write(str)
                    word_list.clear()
