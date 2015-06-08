from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restraunts import views

urlpatterns = [
	url(r'^', views.RestrauntList.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)