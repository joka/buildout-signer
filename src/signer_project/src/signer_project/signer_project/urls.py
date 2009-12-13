from django.conf.urls.defaults import *
from django.contrib import admin
from signer.urls import urlpatterns as signer_urlpatterns
from signer_facebook.urls import urlpatterns as signer_facebook_urlpatterns
admin.autodiscover()

#admin interface
urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    )
# signer_facebook 
urlpatterns += signer_facebook_urlpatterns
# signer 
urlpatterns += signer_urlpatterns

