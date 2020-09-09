from cbvApp import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('newstudents', views.StudentViewSet)

# as_view() is used for class based operations
urlpatterns = [
    # path('cstudents/', views.StudentList.as_view()),
    # path('cstudents/<int:pk>', views.StudentDetail.as_view()),
    path('', include(router.urls))
]
