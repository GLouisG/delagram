from django.conf.urls import url
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('^$',views.landing,name='landing'),  
    url(r'^new/post$', views.new_post, name='new_post'),
    url(r'^comments/(\d+)', views.comment, name='comment'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^you/', views.you, name="you"), 
    url(r'^like/(\d+)', views.like, name="like"),  
    url(r'^search/',  views.search_results, name='search_results'),
    url(r'^bio/', views.bio, name='bio'),
    path("followToggle/<str:name>/",views.followToggle, name="followToggle"),
    url(r'^update/profile$', views.update_profile, name='update_profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)