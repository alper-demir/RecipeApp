from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    image = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    link = models.CharField(max_length=30,default='maincourse')

    def __str__(self):
        return self.title

class maincoursedb(models.Model):
    title = models.CharField(max_length=30)
    image = models.CharField(max_length=30)
    description = models.TextField(max_length=850)
    category = models.CharField(max_length=25)
    time = models.CharField(max_length=20)
    descriptiondetail = models.TextField(max_length=1300)
    ingredient = models.TextField(max_length=450)

    def __str__(self):
        return self.title

class sweetdb(models.Model):
    title = models.CharField(max_length=30)
    image = models.CharField(max_length=30)
    description = models.TextField(max_length=850)
    category = models.CharField(max_length=25)
    time = models.CharField(max_length=20)
    descriptiondetail = models.TextField(max_length=1300)
    ingredient = models.TextField(max_length=450)

    def __str__(self):
        return self.title

class vegetabledb(models.Model):
    title = models.CharField(max_length=30)
    image = models.CharField(max_length=30)
    description = models.TextField(max_length=850)
    category = models.CharField(max_length=25)
    time = models.CharField(max_length=20)
    descriptiondetail = models.TextField(max_length=1300)
    ingredient = models.TextField(max_length=450)

    def __str__(self):
        return self.title