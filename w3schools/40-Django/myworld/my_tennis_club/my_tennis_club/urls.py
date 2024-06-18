from django.urls import path
from . import views

urlpatterns = [
    path('members/', veiws.members, name='members'),
]
