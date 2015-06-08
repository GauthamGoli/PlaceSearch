from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.authtoken import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^restraunts/', include('restraunts.urls')),
    url(r'^api-token-auth/',views.obtain_auth_token),
)
