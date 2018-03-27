from django.conf.urls import url

from . import views

app_name = 'spravaPoli'
urlpatterns = [
    url(r'^$', views.GeneralView.prehladPola, name='prehlad pola'),
    url(r'^cast/(?P<cast_id>[0-9]+)/$', views.CastView.prehladCasti, name='prehlad casti'),
    url(r'^cast/(?P<cast_id>[0-9]+)/(?P<cyklus_id>[0-9]+)/nova-vysadba/$', views.CastView.novaVysadba, name='nova vysadba'),
    url(r'^cast/(?P<cast_id>[0-9]+)/(?P<cyklus_id>[0-9]+)/novy-zber/$', views.CastView.novyZber, name='novy zber'),
    url(r'^nova-cast/$', views.GeneralView.novaCast, name='nova cast'),
    url(r'^plodina/(?P<plodina_id>[0-9]+)$', views.GeneralView.prehladPlodiny, name='prehlad plodiny'),
    url(r'^nova-plodina/$', views.GeneralView.novaPlodina, name='nova plodina'),
]