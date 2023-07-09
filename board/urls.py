from django.urls import path
from .views import *

app_name = 'board'

urlpatterns = [
    path('', BoardList.as_view()),
    path('university/', BoardUniversity.as_view()),
    path('university/<str:university>/', BoardUniversityDetail.as_view()),
    path('<int:pk>/', BoardDetail.as_view()),
    path('<int:pk>/update/', BoardDetailUpdate.as_view()),
    path('<int:pk>/destroy/', BoardDetailDestroy.as_view()),
    path('<int:post>/comments/', CommentsList.as_view()),
    path('<int:post>/comments/<int:id>/', CommentsDetail.as_view()),
    path('<int:post>/comments/<int:id>/update/', CommentsUpdate.as_view()),
    path('<int:post>/comments/<int:id>/destroy/', CommentsDestroy.as_view()),
]