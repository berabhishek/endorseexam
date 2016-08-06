from __future__ import unicode_literals

from django.db import models
from examdist.models import User_Personal
# Create your models here.
class User_Personal(models.Model):
	name = models.ForeignKey(User_Personal, on_delete = models.CASCADE)
	quote = models.TextField("Thought")
	date_published = models.DateTimeField('date published')
	verify = models.BooleanField('Authentic',default = False)
	def __str__(self):
		return str(self.name)+" "+str(self.quote)
