from django.db import models

# Create your models here. # better to deal with python than with sql
class Poll(models.Model): # a table  -- Poll in our db
    text = models.CharField(max_length=255)
    pub_date = models.DateField() #these are columns/attributes 
    #now we make migrations since we updated our database

    def __str__(self):
        #for customizing
        return self.text
        