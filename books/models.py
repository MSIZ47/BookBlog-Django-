from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):    # when we have an instance of the class we use this as an url to get some url
        return reverse('book_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    text = models.TextField()
    book = models.ForeignKey(Book, models.CASCADE)
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


