from django.db import models



class Category(models.Model):
    PARENT_CHOICES = [
        ('classic_historic', 'سبک‌های کلاسیک و تاریخی'),
        ('modern_contemporary', 'سبک‌های مدرن و معاصر'),
        ('cultural_regional', 'سبک‌های فرهنگی و منطقه‌ای'),
        ('abstract_conceptual', 'سبک‌های انتزاعی و مفهومی'),
        ('specialized_technical', 'سبک‌های تخصصی و تکنیکی'),
        ('special_new', 'سبک‌های خاص و جدید'),
        ('subject_based', 'دسته‌بندی موضوعی'),
    ]

    name = models.CharField(max_length=255, unique=True)
    parent_category = models.CharField(
        max_length=50,
        choices=PARENT_CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
    


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.category.name}"
    
