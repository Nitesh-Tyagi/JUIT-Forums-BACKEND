from django.db import models
import datetime
# Create your models here.
class Post(models.Model):
	text = models.TextField()
	created_date = models.DateField(default=datetime.date.today())
	created_on = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering = ['created_on']