from django.conf.urls import url
from .views import CreateUserView,UserView,SendsmsCreate,SendsmsList

urlpatterns = [
    # users
    url(r'^user/', CreateUserView.as_view(),
        name='use-create'),
    url(r'^users/', UserView.as_view(),
        name='use-list'),
    # sms
    url(r'^send/', SendsmsCreate.as_view(),
        name='sendsms-create'),
    url(r'^list/', SendsmsList.as_view(),
        name='sendsms-list'),        
        
]
