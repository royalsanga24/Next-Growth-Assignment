from django.db import models
from django.core.validators import FileExtensionValidator


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class App(models.Model):
    CATEGORY_CHOICES = (
    ('entertaiment','Entertainment'),
    )
    SUB_CATEGORY_CHOICES = (
    ('social media','Social Media'),
    ('games', 'Games'),
    ('finance','Finance'),
    ('education','Education'),
    ('other','Other'),
    )
    name = models.CharField(max_length=100, blank=False, unique=True)
    link = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=False)
    sub_category = models.CharField(max_length=20, choices=SUB_CATEGORY_CHOICES, blank=False)
    icon = models.ImageField(upload_to=upload_to, blank=True, null=True, validators=[FileExtensionValidator(['png','jpg','gif','jpeg'])])

    def __str__(self):
        return self.name
    
class AppModel(models.Model):
    CATEGORY_CHOICES = (
    ('entertaiment','Entertainment'),
    )
    SUB_CATEGORY_CHOICES = (
    ('social media','Social Media'),
    ('games', 'Games'),
    ('finance','Finance'),
    ('education','Education'),
    ('other','Other'),
    )
    name = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=False)
    sub_category = models.CharField(max_length=20, choices=SUB_CATEGORY_CHOICES, blank=False)
    

    def __str__(self):
        return self.name