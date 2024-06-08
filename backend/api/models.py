from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now_add means we do not want the date to be inputted. we want it to be provided automatically
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    # CASCADE means deleting the user means deleting all the notes created by the user

    def __str__(self):
        return self.title
