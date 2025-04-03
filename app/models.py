from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Book(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
