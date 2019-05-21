from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pup_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pup_date_pretty(self):
        return self.pup_date.strftime('%b %e %Y')