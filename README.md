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


## Setup
The first thing to do is to clone the repository:

```sh
$ git clone git@github.com:maracasabat/Personal-Assistant-WEB.git
$ cd assistant
```

Activate virtual environment and install dependencies:

```sh
$ poetry shell
(env)$ poetry install
```

Once `poetry` has finished downloading the dependencies:
```sh
(env)$ cd assistant
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/.
