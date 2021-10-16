README
Runserver
python manage.py runserver_plus --cert-file cert.crt


Social Website assignment from Django 3 By Example text book
using Python and Django framework. 

pip install Django
pip install Pillow
pip install social-auth-app-django
pip install django-extensions
pip install werkzeug
pip install pyOpenSSL

Chapter 4 Issues I had:

There were issues with copying text from the book - multiple
examples had incorrect syntax when adding html 
pages. The book uses double quotes "" but requires 
single quotes ''. This may just be a version difference.

Also, when trying to implement the authentication.html within account file, and adding: 

AUTHENTICATION_BACKENDS = [
    'account.authentication.EmailAuthBackend',
]

I receive an error ModuleNotFoundError: No module named 'account.authentication'
I found that I was placing the authentication file in the wrong account file directory.

The book also doesn't give you an example 
of what the newly changed hosts file should look like when 
adding mysite.com as a domain name when running off of 
localhost. I had to look up what I needed to add 
and where from a 3rd party site. 

I also had an issue implementing google authentication. I found that I didnt add the custom URl site to google.


After creating the images show up in the admin list. I wasn't able to click on images. It would give me an error stating that a column doesn't exist. I removed all of the migration files and deleted the 
db.sqlite3 file. I reran all of the migrations for each app and everything worked fine after that.


I couldnt get some javascript and ajax syntax correct - was showing as errors when copy and pasting from the book and giving an error when running the application....
---------------------------------------------------------------------------------


Chapter 4 - Building a Social Website

This chapter covers the following topics:

Using the Django authentication framework
Creating user registration views
Extending the user model with a custom profile model
Adding social authentication with Python Social Auth

Chapter 5 - Sharing Content on Your Website

Creating many-to-many relationships
Customizing behavior for forms
Using jQuery with Django
Building a jQuery bookmarklet
Generating image thumbnails using easy-thumbnails
Implementing AJAX views and integrating them with jQuery
Creating custom decorators for views
Building AJAX pagination

Chapter 6 - Tracking User Actions

Building a follow system
Creating many-to-many relationships with an intermediary model
Creating an activity stream application
Adding generic relations to models
Optimizing QuerySets for related objects