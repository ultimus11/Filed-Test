from django.conf.urls import url,include
from .views import GETAPIView
from .views import CREATEAPIView
from .views import UPDATEAPIView
from .views import DELETEAPIView
urlpatterns = [
    url('GET/', GETAPIView.as_view()),
    url('CREATE/', CREATEAPIView.as_view()),
    url('UPDATE/', UPDATEAPIView.as_view()),
    url('DELETE/', DELETEAPIView.as_view()),
]
'''
As recomended only four Endpoints are Used
'''