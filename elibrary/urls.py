from django.conf.urls import patterns, include, url

from elibrary.views import AuthorListView, AuthorDetailView, BookListView, BookDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ebooking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^authors/$', AuthorListView.as_view(), name='author-list'),
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^ksiazki/$', BookListView.as_view(), name='book-list'),
    url(r'^ksiazki/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book-detail'),
)
