from django.conf.urls import url
from .views import CreateUserView

urlpatterns = [
    url(r'^user/', CreateUserView.as_view(),
                                        name='use-create'),
]
