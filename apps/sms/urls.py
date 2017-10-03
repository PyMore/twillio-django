from django.conf.urls import url
from .views import CreateUserView,UserView

urlpatterns = [
    url(r'^user/', CreateUserView.as_view(),
        name='use-create'),
    url(r'^users/', UserView.as_view(),
        name='use-list')
]
