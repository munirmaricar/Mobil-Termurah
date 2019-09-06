# PPW Starterpack

## About This Pack

**This Is**
A blank starting project for your web development course in FASILKOM UI. (_note the word blank, you still have to configure models, forms, etc by yourself if you intend to use so,_)

**This is NOT**
This is not a Django Template, this starterpack **does not** contain premade models, forms, etc as mentioned above.

**Disclaimer**
This starterpack is made to tailor your experience during your PPW class so you can focus on implementing your beautiful and awesome ideas instead of geeking out with the settings. Use this starterpack to learn about Django, Heroku, and Gitlab integration and maybe build one your own someday.

## Features

- Configured staticfiles settings
- Pre-configured Gitlab CI yml file
- Base HTML and CSS already linked together
- Requirements.txt provided

## Instructions

### Setting Up

1. Clone this repo to your directory
   `git clone https://gitlab.com/jonathanfilbert/django-ppw-starter.git`
2. Navigate to the cloned project
3. Create a new python environment
   `python3 -m venv Env`
4. Activate the environment
   **Mac / Ubuntu**
   `source Env/bin/activate`
   **Windows**
   `Env/Scripts/activate`
5. Install the dependencies
   `pip3 install -r requirements.txt`
6. Migrate the Django project
   `python3 manage.py makemigrations`
   `python3 manage.py migrate`
7. Run the project
   `python3 manage.py runserver`
8. Go to your browser and type in
   `http://localhost:8000/`
   **You should see the page**
   ![](https://i.imgur.com/wyjn2d2.png)

### Renaming

**Please rename the project so you won't get caught with plagiarism**

1. Rename the **starter** folder into your project name
2. Go to **manage.py** and rename this line
   `` `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "starter.settings")` ``
   change the word **starter** into your project name
3. Go to **your_project_name/settings.py**
   Change **starter** into your project name from these various lines
   `` `ROOT_URLCONF = 'starter.urls'` ``
   `` `WSGI_APPLICATION = 'starter.wsgi.application'` ``
4. Go to **wsgi.py** and rename the word starter to your project name
   `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "starter.settings")`
   **Just to make sure, search for any starter word in your project and rename it to your project name**. _except for the readme file obv._

### Using this starterpack

Everything's configured so you can start writing your HTML/CSS/models ASAP.
**HTML**
Go to tugas/templates/pages/index.html and start implementing your website
** CSS**
Go to static/css/main.css and start writing your css
**Images**
Go to static/assets and start placing your own image
Refer to your image in the HTML by using
`<img src="{% static 'assets/your_image_name.jpg' %}">`
**Javascript**
Go to static/js and start writing your own javascript

### Deploying

This starterpack is already preconfigured to work on PPW Fasilkom UI pipeline, which is Gitlab - Heroku.

1. **Making new Heroku Project**
   Head over to heroku.com new-create new app
   rename the app (**We'll need this app name later on**)
   Click on your profile - Account settings
   scroll down until you find API KEY, reveal and copy the value to the clipboard (**We'll need this later on**)<br/>
2. **Making a Gitlab repo**
   Go to gitlab.com and new project, and create a new project
   Click your newly created repo and go to settings - CI/CD
   Search for **Variables** and click **expand**
   Key = 'HEROKU_API_KEY' (without the quotation)
   Value = the API KEY Value in step 1 that you copied from Heroku

3. **Small config in your project**
   Edit the **gitlab-ci.yml** file in your project, change this line
   `--app=ppwstarter`
   to
   `--app=your_heroku_app_name_in_step_1`
4. **Deploying**
   1. navigate to your directory using terminal
   2. `git remote rename origin upstream`
   3. `git remote add origin URL_TO_GITLAB_REPO`
   4. `git add .`
   5. `git commit -m "YOUR_COMMIT_MESSAGE_HERE"`
   6. `git push origin master`
   7. Now head over to your repo in Gitlab, and CI/CD - Pipelines, and you should see the pipeline starting
   8. If the deploy is done, your url should appear in the bottom of the console.
   9. Your url should look like
      `your_app_name.herokuapp.com`
   10. Happy hacking!

**Should there be any questions / contributions / issues / additions, feel free to add Issues or contact me on LINE, or just message me at hello@jofil.tech**
