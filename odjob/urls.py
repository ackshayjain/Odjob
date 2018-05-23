from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^', include('home.urls',namespace='home')),
    url(r'^admin/', include(admin.site.urls)),
]
