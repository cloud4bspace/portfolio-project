from django.db import models

class Contact(models.Model):
    surname = models.CharField(max_length=200)
    forename = models.CharField(max_length=200)
    birthDate = models.DateTimeField() # TODO: eigentlich DateTimeField
    provileImage = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.forname + " " + self.surname
