from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
import horta.api

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(horta.api.MediaResource())
v1_api.register(horta.api.GardenResource())
v1_api.register(horta.api.ParcelResource())
v1_api.register(horta.api.BedResource())
v1_api.register(horta.api.SpeciesResource())
v1_api.register(horta.api.PlantationResource())
v1_api.register(horta.api.ZoneResource())
v1_api.register(horta.api.WorkSessionResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hortapp.views.home', name='home'),
    # url(r'^hortapp/', include('hortapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'api/', include(v1_api.urls)),
)
