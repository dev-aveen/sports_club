from django.db import models

class Quote(models.Model):
    author = models.CharField(max_length=100)
    maxim = models.TextField()
    is_featured = models.BooleanField(default=False)

    class Meta:
      def __str__(self):
        return self.author
      