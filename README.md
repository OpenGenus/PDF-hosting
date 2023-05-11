# BookStacks

![UI Screenshot](https://ik.imagekit.io/8mch78q847k/Screenshot_from_2023-05-03_16-38-34_k21fIang9.png?updatedAt=1683121209694)

![Upload Feature Screenshot](https://ik.imagekit.io/8mch78q847k/pdf_library_screenshot_3_glyrWG-Yk.png?updatedAt=1681628914852)

A community driven information sharing platform that allows users to preserve and share knowledge through uploading uploading books, research papers, e.t.c

## Create a virtual environment

A virtual environment is isolated environment 

### Using python venv module

`python -m venv pdf_library`

The command creates a virtual environment with the name 'pdf_library'. A folder with the name 'pdf_library' is created in the current working directory. This works for python >= 3.3

### Using virtualenv

`virtualenv --python=/usr/bin/python3 pdf_library`

### Activate virtual environment

`source pdf_library/bin/activate`

## Install dependencies 

`pip install -r requirements.txt`

## Run application

`cd [project directory]`
`python manage.py runserver`

Visit http://localhost:8000 in your browser
