from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=225)
  slug = models.SlugField()

  class Meta:
    ordering = ('name',)

  def __str__(self) -> str:
    return self.name

class Product(models.Model):
  category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
  name = models.CharField(max_length=225)
  slug = models.SlugField()
  description = models.TextField(blank=True,null=True)
  price = models.DecimalField(max_digits=10,decimal_places=2)
  created_at = models.DateField(auto_created=True)

  class Meta:
    ordering = ('-created_at',)

  def __str__(self) -> str:
    return self.name