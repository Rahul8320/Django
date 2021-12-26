from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=300)
    product_catagory = models.CharField(max_length=50, default="")
    product_subCatagory = models.CharField(max_length=50, default="")
    product_price = models.IntegerField()
    product_publicationDate = models.DateField()
    product_image = models.ImageField(upload_to='shop/images', default="")
    
    def __str__(self):
        return self.product_name
    