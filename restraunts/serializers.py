#from django.forms import widgets
#from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from restraunts.models import Restraunt



class RestrauntSerializer(GeoFeatureModelSerializer):
	""" A class to serialize locations as GeoJSON compatible data """

	class Meta:
		model = Restraunt
		geo_field = "coordinates"
		id_field = False
		fields = ("name",)