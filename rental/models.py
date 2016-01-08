from django.db import models
from django.contrib.auth.models import User
from shelf.models import BookItem

from django.utils.timezone import now

# Create your models here.

class Rental(models.Model):
	who = models.ForeignKey(User)
	what = models.ForeignKey(BookItem)
	when = models.DateTimeField(default=datetime.now())
	returned = models.DateTimeField(null=True, blank=True)

	def __str__ (self):
		return ''
	    
		