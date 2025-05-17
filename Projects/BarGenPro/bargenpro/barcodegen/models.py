from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    code_type = models.CharField(max_length=20)
    code_value = models.CharField(max_length=50)
    barcode_image = models.ImageField(upload_to='barcodes/', blank=True)

    def __str__(self):
        return f"{self.name} ({self.code_type}: {self.code_value})"
