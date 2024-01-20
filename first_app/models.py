from django.db import models

# Create your models here.

class ExampleModel(models.Model):
    field1 = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, default = 'NULL')
    date_field = models.DateField(default = 'NULL')
    date_time_field = models.DateTimeField(default = 'NULL')
    duration_field = models.DurationField(default = 'NULL')
    email_field = models.EmailField(default = 'name@gmail.com')
    file_field = models.FileField(upload_to='files/')
    slug_field = models.SlugField(default = 'NULL')
    text_field = models.TextField(default = 'NULL')

    def __str__(self):
        return f'Roll:{self.field1} - Name:{self.field2}'