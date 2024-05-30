from django.db import models


# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Archives(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    categories = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Author(TimeStampedModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    profession = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SubPost(TimeStampedModel):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, related_name='sub_posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class Travel(TimeStampedModel):
    image = models.ImageField(upload_to="travel/%Y/%m/%d")
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    categories = models.ForeignKey(Category, related_name='travels', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class About(TimeStampedModel):
    profession = models.CharField(max_length=255)
    image = models.ImageField(upload_to="about/%Y/%m/%d")
    description = models.TextField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contact(TimeStampedModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


class Contact1(TimeStampedModel):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address
