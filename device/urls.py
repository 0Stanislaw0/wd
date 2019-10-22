from django.urls import path,include
from . import views
from .router import router

urlpatterns = [
    path('', views.ShowDeviceView.as_view(), name ='show'),
    path(r'detail/<int:pk>/', views.DeviceDetailView.as_view(), name='device_detail'),
    path(r'detail/add/', views.CreateDeviceView.as_view(), name='detail-add'),
    path(r'device/new/', views.device_new, name='device-new'),
    path(r'device/<int:pk>/update/', views.UpdateDeviceView.as_view(), name='update'),
    path(r'device/<int:pk>/delete/', views.DeLeteDeviceView.as_view(), name='delete'),
    path('api/', include(router.urls)),
  ]
