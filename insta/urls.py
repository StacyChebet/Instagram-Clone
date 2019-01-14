from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.login, name="login"),
    url(r'^home$', views.index, name="index"),
    url(r'^accounts/profile/$', views.profile, name="profile"),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^search/$', views.search_results, name="search"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)