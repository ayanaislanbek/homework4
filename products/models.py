from django.db import models

class Products(models.Model):
    name_models = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product/')
    description = models.TextField()
    TYPE_PRODUCTS = (
        ("Books", "Books"),
        ("Musical instruments","Musical instruments"), 
        ("Office supplies","Office supplies" )

    )
    type_products = models.CharField(max_length=50, choices= TYPE_PRODUCTS,default="Books",verbose_name="category" )
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    warehouse = models.PositiveIntegerField(default=1 , verbose_name="quantity")
    manual = models.FileField(upload_to='manuals/', blank=True, null=True, verbose_name="instructions PDF")
    video_review = models.URLField(blank=True, null=True, verbose_name="video review link")
    product_url = models.URLField(blank=True, null=True, verbose_name="product link")          

    def __str__(self):
        return self.name_models
    


class Reviews(models.Model):
    post = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="review")
    MARKS = (
        ("🤍", "🤍"),
        ("🤍 🤍 ", "🤍 🤍 "),
        ("🤍 🤍 🤍", "🤍 🤍 🤍"),
        ("🤍 🤍 🤍 🤍", "🤍 🤍 🤍 🤍"),
        ("🤍 🤍 🤍 🤍 🤍", "🤍 🤍 🤍 🤍 🤍")
    )
    marks = models.CharField(max_length=1000, choices=MARKS, default="🤍")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.post}:{self.marks}'
    