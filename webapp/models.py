from django.db import models

# Create your models here.

class userDetails(models.Model):
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Active = models.BooleanField(null=False)
 
    def __str__(self):
        return self.Email
    class Meta:
        db_table = 'UserDetail'
        verbose_name = 'UserDetail'

class blog(models.Model):
    Title = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    Pub_date = models.DateField()
    Author = models.ForeignKey(userDetails, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title
    class Meta:
        db_table = 'Blog'
        verbose_name = 'Blog'
