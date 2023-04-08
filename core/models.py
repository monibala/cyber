from django.db import models

# Create your models here.



class Contact(models.Model):
    full_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField()
    subject = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.full_name
    
    
class Knowledge(models.Model):
    # category = models.ForeignKey(Category, on_delete= models.CASCADE, default=1)
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default=True, upload_to = 'knowledge')
    date = models.DateTimeField(auto_now_add=True)
    
    
