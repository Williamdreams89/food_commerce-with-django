from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Item(models.Model):
    LABELS = [
        ["BestSeller","BestSeller"],
        ["New","New"],
        ["Spicy","Spicy"]
    ]

    LABEL_COLORS = [
        ["primary","primary"],
        ["secondary","secondary"],
        ["danger", "danger"],
        ["warning", "warning"],
        ["info","info"]
    ]

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    description = models.CharField(max_length=70)
    price = models.FloatField(default=5.00)
    pieces = models.IntegerField(default=1)
    instructions = models.CharField(max_length=80)
    label = models.CharField(max_length=50, choices=LABELS)
    label_color = models.CharField(max_length=50, choices=LABEL_COLORS)
    slug = models.SlugField(default="food_item")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


class CartItems(models.Model):
    STATUS = [
        ['Active','Active'],
        ['Delivered', 'Delivered']
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=50, choices=STATUS)
    ordered_date = models.DateField(default=timezone.now)
    delivery_date = models.DateField(default=timezone.now)
    c_slug =models.SlugField()

    class Meta:
        verbose_name_plural = 'CartItems'
    

    def __str__(self):
        return self.item.title + str(self.ordered_date)
    
    
