Here we do a resume uploader project in Django:


In the Date of Birth field.

We can either use the attrs: {'type': 'data'} in the forms.py file
Or
We can use the jquery-ui.css and jquery-ui.js and use the 'datepicker' as id

attrs: {'id': 'datepicker'}

Both will work.

To view the image file and download the uploaded resume from the admin panel, you need to do few changes in the urls.py file

you need to add a static() function to the url patterns

Take a look in to the urls.py file in the main project folder(resumeuploader).

Also, if you wish to keep all the media files uploaded by the user in to a seperate file then you can use 

MEDIA_URL = '/media/'
MEDIA_ROOT= BASE_DIR / 'media'

in the settings.py file. We havent used this here.
But we have implemented the media directory in the imageuploader project. Take a look in to it.
We will also do it in here in this project(resumeuploader) later.

Note: The 'profileimg' and 'doc' folder are automatically created by django. Since you have given these names to 'upload_to=' options
inside the models.py while creating the model, these will be automatically created.


-----------------------------


If you want the change the name of the image and/or the resume before saving it, I tried and could not do it.

But there are methods to do it, in the stack overflow , may be we need to take a closer look in to it and implement it later.

As of now, of two user is uploading the image or resume with same name, the django by default is hashing it with the ramdom value
to the end of file and saving, so that there wont be any clash of names.

If you want to change it, you do so, by attaching the name and time of save or even use the uuid value to append to the name to have 
a unique name. This we need to take a more detail look, then only we can implement it.

---------------------

How to use your custom filters?

Why to use custom filters?

In the Preferred Job Cities: sectin we are getting a list of cities inside the square brackets. As a python developer we may know
that it is a list.
But for the front end, its not common to know these things.
Hence, it is better to show up the city names in plain text, instead of being inside the square brackets.

To do so, we need to use the custom filters to remove the square brackets and '' .

You can use the custom filter (which you have created inside the templatetags folder) in your html file.

Make suere u have the name of the folder as 'templatetags' only.
And make sure you have __init__.py file inside this folder.
Having this file __init__.py makes this folder to see as an package.
Inside this templatetags folder create a myfilter.py file and write your logic.

And make sure you restart your server in order for the templatetags to take effect.

---------------------------------

Now when we delete a instance from the model, all the data gets deleted, but the files inside the profileimg and doc are still alive.
Its not cleared on its own. We need to write the code/logic to clear that data as well.

There are few ways to do it.

In our imageuploaded project we did this by overriding the delete method in the models.py file, where , when delete() is called
it will again call the super().delete() method to delete all the media files.
Example below:
class Image(models.Model):
    photo = models.ImageField(upload_to='myimage')
    # photo_caption = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.photo.delete()
        super().delete(*args, **kwargs)  # Call the "real" delete() method.


-------------------------------------------

Another method is to use the signals to delete or update a media file whenever that instances gets deleted or updated.

-----------------------------------------

Another method is to do it in the serverside command prompt. This is taught by geekyshows.

for that you need to install django-unused-media first

pip install django-unused-media


After installing, we need to mention it inside the settings.py file
under the INSTALLED_APPS


To clean up all the unused media files run the following command

python manage.py cleanup_unused_media

Inorder to execure the above command, you must be inside the project folder, meaning where the manage.py resides.

----------------------------------

Now lets try to have the media files in a seperate folder called media inside the project folder.

First we need to say it in the settings.py file

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


Note: The 'media' folder and the subfolders of media folder - 'profileimg' and 'doc' are created automatically by django.









