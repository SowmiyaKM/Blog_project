from django.db import models
from django.utils.text import slugify

#Creating category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content =models.TextField()
    img_URL = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title 

class Aboutus(models.Model):
    content=models.TextField()

class Submission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

