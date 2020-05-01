from django.urls import include, path
from .views import TrackerList, TrackerDetail

urlpatterns = [
    path('<int:pk>/', TrackerDetail.as_view()),
    path('', TrackerList.as_view()),
]