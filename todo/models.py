from __future__ import unicode_literals

from django.db import models
from datetime import date
# Create your models here.

class Todo(models.Model):
	title = models.CharField(max_length=32, unique=True, blank=True, null=True)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True, editable = True)

	def __unicode__(self):
		return self.title

	class Meta:
		db_table = 'todo'
