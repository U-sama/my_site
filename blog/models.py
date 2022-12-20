from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.caption
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=150)
    exerpt = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, primary_key=True)
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, related_name="posts", null=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField(Tag)