from django.db import models
from django.conf import settings


class Note(models.Model):
    class Meta:
        ordering = ('updated_at',)

    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )

    def __str__(self):
        return self.title


# settings.AUTH_USER_MODEL - returns a string (the location of the User model) e.g. accounts.User - use in models.py
# get_user_model() - returns the ACTUAL model class, not a string
