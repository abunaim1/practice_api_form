from django.db import models

# Create your models here.

class ExampleModel(models.Model):
    field1 = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, default = 'Rahim')
    date_field = models.DateField(default='2024-01-20')
    date_time_field = models.DateTimeField(default='2024-01-20T12:00:00')
    duration_field = models.DurationField(default='1 day')
    email_field = models.EmailField(default='your_default@example.com')
    slug_field = models.SlugField(default='default-slug')
    text_field = models.TextField(default='Default text content.')
    