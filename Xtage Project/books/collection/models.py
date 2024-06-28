from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    google_books_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255, null=True, blank=True)
    thumbnail_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f'{self.user.username} likes {self.book.title}'

class UserCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collection')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='in_collections')
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f'{self.user.username} saved {self.book.title}'
