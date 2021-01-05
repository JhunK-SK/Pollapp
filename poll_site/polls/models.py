from django.db import models

class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=50)
    option_two = models.CharField(max_length=50)
    option_three = models.CharField(max_length=50, null=True, blank=True)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.question