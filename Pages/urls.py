from . import views
from django.urls import path

urlpatterns = [
    path('', views.reviewlist, name="home"),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
]
