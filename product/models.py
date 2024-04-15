from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=60,unique=True)
    price = models.IntegerField(default=0)
    images = models.ImageField(upload_to="product/product_images", default='product.jpg')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=9)
    description = models.CharField(default='',blank=True,null=True,max_length=250)
    
    @staticmethod
    def get_product_by_id(ids):
        return Products.objects.filter(id__in= ids)
    
    @staticmethod
    def get_all_products():
        return Products.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()
        
    def __str__(self):
        return self.name