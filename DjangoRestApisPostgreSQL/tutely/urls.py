from django.conf.urls import url 
from tutely import views 
 
 
# /api/tutorials: GET, POST, DELETE
# /api/tutorials/:id: GET, PUT, DELETE
# /api/tutorials/published: GET

urlpatterns = [ 
    url(r'^api/tutorials$', views.tutorial_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorials/published$', views.tutorial_list_published)
]