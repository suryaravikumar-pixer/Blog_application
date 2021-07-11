
# Django blog application

A Blog application with Django that allows users to create, edit, and delete posts. The homepage will list all blog posts, and there will be a dedicated detail page for each individual post. 


## Documentation


## Set up a virtual environment and activate

I have done all this in my git bash terminal. Make dir for this proejct, then follow the below steps
```python
  python -m venv venv
  source venv/Scripts/activate
```

## Run Locally

 Clone the project

```bash
  git clone https://github.com/suryaravikumar-pixer/Blog_application
```

Go to the project directory

```bash
  cd Blog_application
```

Install dependencies

```bash
  pip install django
  pip install pillow
  pip install tree
```

Start the project and an app

- Use the period (.) after the project name so it does not create another proejct dir name

```bash
  djago-admin startproject djago_application .
  python manage.py startapp blog
```

Start the server
    
- this stats an web development server at http://127.0.0.1.8000/ or http://localserver:8000. To stop server use Ctrl+C

```bash
  python manage.py runserver
```


## .gitignore
- Paste the files that you do not want track by the git and following link will have the gitignore files of python 
[gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore)
  
```txt file
say like venv, db.sqlite3, env/, and etc
```

## requirements.txt
- The below command sumup the all installed packges into the requirements file.
```bash
pip freeze -> requirements.txt
```


## Bootstrap link
[Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template) 
- Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains CSS- and JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components.
 
## Authors

- [Corey Schafer](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&ab_channel=CoreySchafer)

  
