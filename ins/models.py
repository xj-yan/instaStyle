from django.db import models
from django.contrib.auth.models import AbstractUser

from django.urls import reverse, reverse_lazy
from imagekit.models import ProcessedImageField


# Create your models here.
class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )


class Post(models.Model):
    author = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name='my_posts'
    )
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        # return reverse("post_detail", kwargs={"pk":self.pk})
        return reverse("post_detail", args=[str(self.id)])

    def get_like_count(self):
        return self.likes.count()


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
        )
    user = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        )

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return self.user.username + ' likes ' + self.post.title
