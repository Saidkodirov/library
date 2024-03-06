from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length = 250)
    subtitle = models.CharField(max_length = 250)
    body = models.TextField()
    author = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.title}"