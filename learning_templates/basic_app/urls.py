from django.conf.urls import url
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'

urlpatterns=[

    url(r'^online/$',views.online,name='online'),
    url(r'^code/$',views.code,name='code'),
    url(r'^downloads/$',views.downloads,name='downloads'),
    # url(r'^index/$',views.index,name='index'),
    # url(r'^ML/$',views.ML,name='ML'),
    url(r'^photos/$',views.photos,name='photos'),]
