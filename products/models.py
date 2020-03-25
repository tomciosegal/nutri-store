from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default= 1)
    currency= models.CharField(max_length=3, default= "EUR")
    image = models.ImageField(upload_to='images')
    category= models.ForeignKey("products.ProductCategory", blank= True, null= True, on_delete= models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


