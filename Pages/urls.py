from . import views
from django.urls import path

urlpatterns = [
    path('', views.reviewlist, name="home"),
    path('create_review/', views.create_review, name='create_review'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('like/<slug:slug>/', views.ReviewLike.as_view(), name='review_like'),
]
