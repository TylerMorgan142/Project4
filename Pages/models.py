from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Game(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class Review_post(models.Model):
    title = models.CharField(max_length=200, unique=True, default="")
    slug = models.SlugField(max_length=200, unique=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1),
        ]
    )
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='review_like', blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_on"]

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Review_post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"