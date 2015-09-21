from django.conf.urls import patterns, include, url

from oodash.views import homepage
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oodash.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login,name='homepage_login'),
    url(r'^logout/', logout, {'next_page': '/login/'},name='homepage_logout'),
    url(r'^home/', homepage, name='homepage_url'),
)
