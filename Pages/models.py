from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=100)
    body = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='', null=True, blank=True)
    
    def __str__(self) -> str:
        return f"Titulo: {self.titulo}"
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.user} - {self.image}"
    
class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name="reciever", on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField()
    
