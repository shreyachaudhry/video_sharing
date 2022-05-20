from django.db import models  

class Video(models.Model):  
    title = models.CharField(max_length=100)   
    created_date = models.DateField()
    num_likes = models.IntegerField()
    num_dislikes = models.IntegerField()
    class Meta:  
        db_table = "videos"  
        app_label = "videos"

# Create your models here.
