from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=20)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
     return self.body[:50]
class comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    body=models.TextField()
    is_validate=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
     return self.body[:50]
