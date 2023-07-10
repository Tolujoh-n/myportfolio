from django.db import models

class Project(models.Model):
    video_url = models.URLField()
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=255)
    repo_url = models.URLField()
    live_url = models.URLField()
    stacks = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
