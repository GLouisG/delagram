from django.conf.urls import url, path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('^$',views.landing,name='home'),  
    url(r'^new/post$', views.new_post, name='new_post'),
    url(r'^comments/(\d+)', views.comment, name='comment'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^you/', views.you, name="you"), 
    url(r'^like/(\d+)', views.like, name="like"),  
    url(r'^search/',  views.search_results, name='search_results'),
    path("followToggle/<str:name>/",views.followToggle, name="followToggle")
]
