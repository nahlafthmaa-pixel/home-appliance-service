from django.db import models

# Create your models here.
class Collection(models.Model):
    collection_name=models.CharField(max_length=100)
    description=models.TextField()
    collcover=models.CharField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.collection_name