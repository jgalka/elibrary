from django.conf.urls import patterns, include, url
from django.contrib import admin

from contact.views import MessageAddView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ebooking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^elibrary/', include('elibrary.urls', namespace='elibrary')),
    url(r'^contact/$', MessageAddView.as_view()),
)
