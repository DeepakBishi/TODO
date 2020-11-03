from django.conf.urls import url
from myApp import views

app_name = 'myApp'

urlpatterns = [
    url(r'^$', views.homeView, name='home'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^add_list/$', views.createPostView, name='add_list'),
    url(r'^mytodo_list/$', views.listPostView, name='mytodo_list'),
    url(r'^warnings/$', views.showWarningsView, name='warnings'),
    url(r'^mytodo_completed/$', views.listPostCompletedView, name='mytodo_completed'),
    url(r'^mytodo_list/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='mytodo_details'),
    url(r'^mytodo_list/(?P<pk>\d+)/completed$', views.PostCompletedDetailView.as_view(), name='mytodo_completed_details'),
    url(r'^mytodo_list/(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(), name='mytodo_delete'),
    url(r'^mytodo_list/(?P<pk>\d+)/update/$', views.PostUpdateView.as_view(), name='mytodo_update'),
    url(r'^mytodo_list/(?P<pk>\d+)/complete/$', views.listCompleteView, name='mytodo_complete'),
]