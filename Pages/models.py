from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Game(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)


class Review_post(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField()
    likes = models.ManyToManyField(
        User, related_name='review_like', blank=True)
    
    def __str__(self):
        return f"Review for {self.game.title} by {self.user.username}"

    class Meta:
        ordering = ["-created_on"]

    def number_of_likes(self):
        return self.likes.count()