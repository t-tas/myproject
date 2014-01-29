from django.conf.urls.defaults import patterns

#commit###3#
urlpatterns = patterns('mycrm.views',
  (r'^$', 'anasayfaView'),
    (r'^aktiviteler/(?P<slug>[^/]+)/$','anasayfaView'),
    )