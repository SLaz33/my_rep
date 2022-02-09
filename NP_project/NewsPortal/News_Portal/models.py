from django.db import models
from django.contrib.auth.models import User
Petr = Author.objects.create(user = Petr_user)

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self, new_rating):
        self.rating = new_rating
        self.save()

class Post(models.Model):
    news = 'NWS'
    article = 'ART'

    CONTENT = [
        (news, 'НОВОСТЬ'),
        (article, 'СТАТЬЯ')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=3,
                                    choices=CONTENT,
                                    default=news)
    data_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    content_rating = models.IntegerField(default=0)

    def like(self):
        self.content_rating += 1
        self.save()

    def dislike(self):
        self.content_rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    datat_time = models.DateTimeField(auto_now_add=True)
    content_rating = models.IntegerField(default=0)

    def like(self):
        self.content_rating += 1
        self.save()

    def dislike(self):
        self.content_rating -= 1
        self.save()
