from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cuentas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.data_accounts),
    url(r'^detail/(?P<pk>\d+)/$', views.dates_concepts),
    url(r'^suma/(?P<pk>\d+)$', views.sum_expense),
)
