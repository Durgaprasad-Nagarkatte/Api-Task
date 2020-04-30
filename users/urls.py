from .views import UserList, UserDetail
from django.urls import include, path

urlpatterns = [
    path('<int:pk>/', UserDetail.as_view()),
    path('', UserList.as_view()),
]