from django.contrib.gis.db import models

class Restraunt(models.Model):
	"""Holds attributes of Restraunts"""
	name = models.CharField(max_length=50)
	coordinates = models.PointField(null=True)

	# overriding the default manager with a GeoManager instance.
	objects = models.GeoManager()

	# Returns the string representation of the model.
	
	def __unicode__(self):
		return self.name
