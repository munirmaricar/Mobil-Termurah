# PPW Starterpack

## About This Pack
**This Is**
A blank starting project for your web development course in FASILKOM UI.  (*note the word blank, you still have to configure models, forms, etc by yourself if you intend to use so,*)

**This is NOT**
This is not a Django Template, this starterpack **does not** contain models, forms, etc as mentioned above. 

**Disclaimer**
This starterpack is made to tailor your experience during your PPW class. Use this starterpack to learn about Django, Heroku, and Gitlab integration and maybe build one your own someday.

## Features
* Configured staticfiles settings
* Pre-configured Gitlab CI yml file
* Base HTML and CSS already linked together
* Requirements.txt provided

## Instructions

### Setting Up
1. Clone this repo to your directory
``
git clone https://gitlab.com/jonathanfilbert/django-ppw-starter.git
``
2. Navigate to the cloned project
3. Create a new python environment
``
python3 -m venv Env
``
4. Activate the environment
**Mac / Ubuntu**
``
source Env/bin/activate
``
**Windows**
``
Env/Scripts/activate
``
5. Install the dependencies
``
pip3 install -r requirements.txt
``
6. Migrate the Django project
``
python3 manage.py makemigrations
``
``
python3 manage.py migrate
``
7. Run the project
``
python3 manage.py runserver
``
8. Go to your browser and type in
``
http://localhost:8000/
``
**You should see the page**
![](https://i.imgur.com/wyjn2d2.png)

### Renaming
**Please rename the project so you won't get caught with plagiarism**
1. Rename the **starter** folder into your project name
2. Go to **manage.py** and rename this line
``
`os.environ.setdefault("DJANGO_SETTINGS_MODULE", "starter.settings")`
``
change the word **starter** into your project name
3. Go to **your_project_name/settings.py**
Change **starter** into your project name from these various lines
``
`ROOT_URLCONF = 'starter.urls'`
``
``
`WSGI_APPLICATION = 'starter.wsgi.application'`
``
4. Go to **wsgi.py** and rename the word starter to your project name
``
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "starter.settings")
``
**Just to make sure, search for any starter word in your project and rename it to your project name**. *except for the readme file obv.*

### Using this starterpack
Everything's configured so you can start writing your HTML/CSS/models ASAP. 
**HTML**
Go to tugas/templates/pages/index.html and start implementing your website
** CSS**
Go to static/css/main.css and start writing your css
**Images**
Go to static/assets and start placing your own image
Refer to your image in the HTML by using
``
 <img src="{% static 'assets/your_image_name.jpg' %}">
``
**Javascript**
Go to static/js and start writing your own javascript

