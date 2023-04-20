# Personal-Assistant-WEB
The personal WEB-application based on the Web framework - Django.

The application allows you to store your contacts personal data, adding notes, processing your gallery and getting last news.  
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This is your **personal** web-assistant that helps to organise:
* **Ukrainian news** - get in real time all latest Ukrainian news in the categories: Sport, Currency, IT, Fashion and Books.
* **Phone Book** - add new contacts to the phonebook, together with birthday, email and address information. Additional features: edit and delete contacts, announce the next birthdays. Provide an easy contact search.
* **Note Book** - add note together with their title and tags. Additional features: add new tags, quick search by tags.  
* **Gallery** - add your file to the gallery. Provides a possibility of simple and advanced file upload, sort all files by the category. Additional features: adding books with author and book covers, as well as adding photos to the photo gallery.
	
## Technologies
Project is mainly based on:
* Web framework: Django
* Frontend: HTML/CSS, Tailwind.css, Node.js
* Backend: python and JavaScript


## Setup:
* The first thing to do is download [Node.js](https://nodejs.org/en/download) and install it:

* The second thing to do is to clone the repository:

```sh
$ git clone git@github.com:maracasabat/Personal-Assistant-WEB.git
```

Activate virtual environment and install dependencies:

```sh
$ poetry shell
(env)$ poetry install
```

* Once `poetry` has finished downloading the dependencies:

* Create .env file in project root and fill in the file like this example:
```sh
SECRET_KEY=secret_key
ALLOWED_HOSTS=*

POSTGRES_DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

* If you want to use Cloudinary add next steps:
```sh
CLOUD_NAME=cloudinary_NAME
API_KEY=cloudinary_KEY
API_SECRET=cloudinary_SECRET
```
* Or you can choose local storage on file settings.py

```sh
if you use Windows choose next option on file settings.py:
    NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd" # Windows
else:
    NPM_BIN_PATH = '/usr/local/bin/npm'  # MacOS
```   
```sh
First terminal:
(env)$ cd assistant
(env)$ python manage.py migrate
(env)$ python manage.py tailwind install
(env)$ python manage.py tailwind build
(env)$ python manage.py tailwind start
```

```sh
Second terminal:
(env)$ cd assistant
(env)$ python manage.py runserver     
```

And navigate to `http://127.0.0.1:8000/.

## Docker setup

1. Build containers via `docker-compose`:

    ```bash
    docker-compose build
    ```

2. Start containers:

    ```bash
    docker-compose up
    ```

3. Open `http://localhost:8000` in a browser. You should see the main page.

    ```bash
    docker pull maracasabat/assistant
    ```

    ```bash
    docker run -p 8000:8000 maracasabat/assistant
    ```

    ```bash
    https://assistant-maracasabat.koyeb.app/
    ```
