
from django.urls import path
from . import views
urlpatterns = [
    path("",views.login,name="login"),
    path("data/",views.data_html,name='data'),
    path("data/gst_data/",views.gst_page,name ='gst_data')
]