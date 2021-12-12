<p align="center">
  <img src="https://user-images.githubusercontent.com/94374523/145721012-e3920b6d-c9e7-4764-b313-972eb79289e5.png" width="600px" height="300px">
</p>

# Syllabus-condenser
This project is aimed at college students. The main issue with college students is that they don't get enough time to go through the previous years' question papers which is very important as there is a high chance that questions may be repeated and that's exactly where this project comes into place. This project uses the basics of [**Natural Language Processing (NLP)**](https://machinelearningmastery.com/natural-language-processing/) and [**OCR**](https://searchcontentmanagement.techtarget.com/definition/OCR-optical-character-recognition) and creates a simple predictive machine learning model which suggests only the important topics from the syllabus to study. Just upload the PDFs of the syllabus and previous ear question paper and *voilà!!!* you get the most repeated topics from which questions have been asked in past years
## Installation
To run this program type the following commands 
```python
pip install -r requirements
``` 
Confirm the installations and then type the following to migrate the data:
```python
python manage.py migrate
```
Confirm the migration is error free, and then type the following in command prompt and follow the instructions in terminal to create a superuser:
```python 
python manage.py createsuperuser
``` 

## Usage

Now type the following to start the website server in localhost:
```python
python manage.py runserver
```
Now type the following in your browser to access the website:
```python
localhost:8000
```
## Credits  
[<img src="https://img.shields.io/badge/Stack_Overflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white">](https://stackoverflow.com/)  [<img src="https://img.shields.io/badge/GeeksforGeeks-gray?style=for-the-badge&logo=geeksforgeeks&logoColor=35914c">](https://www.geeksforgeeks.org/)  [<img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white">](https://medium.com/)  [<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">](https://pypi.org/)  [<img src="https://img.shields.io/badge/<handle>-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white">](https://www.youtube.com/c/KunalKushwaha/featured) 
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate
