from tokenize import Number
from unicodedata import name
from django.db import models
from django.utils import timezone #for date_posted
from django.contrib.auth.models import User  #for the author
from django.urls import reverse
# Create your models here.

class Query(models.Model):
    name = models.CharField('Your Name', max_length=120)
    contact = models.CharField('Contact Number', max_length=10)
    email = models.EmailField('Your Email Address', max_length=30)
    query = models.TextField('Query', max_length=500)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)  #if the user is deleted the post will be deleted  tooo and vice versa is not true.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
