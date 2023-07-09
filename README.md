# community

# 추가 구현 목록

app_name = 'board'

urlpatterns = [

    # 전체 게시글 조회 (대학 추가)
    path('university/', BoardUniversity.as_view()),

    # 특정 대학의 게시글 조회
    path('university/<str:university>/', BoardUniversityDetail.as_view()),

    # 특정 댓글 조회
    path('<int:post>/comments/<int:id>/', CommentsDetail.as_view()),

    # 특정 댓글 수정
    path('<int:post>/comments/<int:id>/update/', CommentsUpdate.as_view()),

    # 특정 댓글 삭제
    path('<int:post>/comments/<int:id>/destroy/', CommentsDestroy.as_view()),
]
