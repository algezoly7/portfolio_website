from distutils.command.upload import upload
from pydoc import describe
from django.db import models
from django import forms


class Photo(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images')
    position = models.CharField(max_length=50)
    github_link = models.CharField(max_length=500)
    linkedin_link = models.CharField(max_length=500)
    email_link = models.CharField(max_length=500)
    twitter_link = models.CharField(max_length=500)
    cv_link = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "myapp_image3"


class Biography(models.Model):
    project = models.TextField(max_length=700)

    def __str__(self):
        return self.project


class Education(models.Model):
    education_stage = models.CharField(max_length=300)
    place_of_education_stage = models.CharField(max_length=50)

    def __str__(self):
        return self.education_stage


class Projects_photos(models.Model):
    image_title = models.CharField(max_length=50)
    image_field = models.ImageField(upload_to='images')
    describtion = models.TextField(max_length=300)
    link = models.CharField(max_length=50)

    def __str__(self):
        return self.image_title

    class Meta:
        db_table = "myapp_image"


class Publications_photos(models.Model):
    image_title = models.CharField(max_length=50)
    image_field = models.ImageField(upload_to='images')
    describtion = models.TextField(max_length=300)
    link = models.CharField(max_length=50)

    def __str__(self):
        return self.image_title

    class Meta:
        db_table = "myapp_image2"
