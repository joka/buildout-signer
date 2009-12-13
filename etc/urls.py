from django.conf.urls.defaults import *
from signer_facebook.urls import urlpatterns as signer_facebook_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^signer/', include('signer.urls')),

    (r'^admin/', include(admin.site.urls)),


# singer pyfacebook example
urlpatterns += signer_facebook_urlpatterns
#urlpatterns +=    (r'^facebook/', include('signer.pyfacebook_sample.urls')) 

# signer example
from signer.urls import urlpatterns as signer_urlpatterns
urlpatterns += signer_urlpatterns

 
)
