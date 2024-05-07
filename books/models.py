from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Category(models.Model):
      name = models.CharField(max_length=100)
    # Add any additional fields if needed

      def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Add any additional fields if needed

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdfs/')
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    like=models.ManyToManyField(User,blank=True,related_name='liked_books')
    already_read=models.ManyToManyField(User,blank=True,related_name='read_books')
    
def __str__(self):
        return self.title

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username}:{self.content[:30]}'
      
      
