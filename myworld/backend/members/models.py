from django.db import models

# Create your models here.

class Notes(models.Model):
    transcript = models.TextField()
    classifiedNotes = models.ArrayField()
    keywords = models.ArrayField()
    def _str_(self):
        return self.transcript