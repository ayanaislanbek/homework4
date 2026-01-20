from django.db import models
    

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
     return self.name
     



class ClothesModel(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='clothes/')
    brands_name = models.ManyToManyField(Brand)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.title 








