from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length = 50)
    human_name = models.CharField(max_length = 50)
    description = models.TextField()
    
    def __str__(self):
        return self.human_name

class Code(models.Model):
    LANGUAGE_CHOICES = (
        ("c++", "c++"),
        ("py", "python"),
        ("c", "c"),
        ("java", "java"),
        ("c#", "c#"),
        ("js", "javascript")
    )

    DICT_LANGUAGES_CHOICES = dict(LANGUAGE_CHOICES)

    title = models.CharField(max_length = 100)
    createdAt = models.DateTimeField(default = timezone.now)
    updatedAt = models.DateTimeField(default = timezone.now)
    description = models.TextField()
    source = models.TextField()
    tags = models.ManyToManyField(Tag)
    original = models.CharField(max_length = 100)
    language = models.CharField(max_length = 10, choices = LANGUAGE_CHOICES) 

    def __str__(self):
        return self.title

    def human_language(self):
        return self.DICT_LANGUAGES_CHOICES[self.language]

    def full_description(self):
        return f'<div class = "container">{self.description}</div>'
