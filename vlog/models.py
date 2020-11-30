from django.db import models

class Category(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField()
        updated_at = models.DateTimeField(auto_now=True)

class Vlog(models.Model):
        title = models.CharField(max_length=200)
        url = models.CharField(max_length=200)
        description = models.TextField()
        category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now=True)
        updated_at = models.DateTimeField(auto_now=True)

