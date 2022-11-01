from django.db import models

from django.core.validators import MinLengthValidator


# Create your models here.
class Tag(models.Model):
    captions = models.CharField(max_length=50)

    def __str__(self):
        return self.captions


class Author(models.Model):
    firstName = models.CharField(max_length=80)
    lastName = models.CharField(max_length=80)
    emailAddress = models.EmailField()

    def author_name(self):
        return f'{self.firstName} {self.lastName}'
    def __str__(self):
        return self.author_name()


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", null=False, unique=True, db_index=True)
    content = models.TextField(default="", null=False, validators=[MinLengthValidator(150)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)
