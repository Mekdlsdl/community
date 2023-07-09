from .models import Board, Comments
from .serializers import BoardSerializer, CommentSerializer, BoardDetailSerializer, CommentDetailSerializer, BoardUniversitySerializer, BoardUniversityDetailSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveAPIView


# 전체 블로그 조회
class BoardList(ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


# 전체 블로그 조회 (대학 추가)
class BoardUniversity(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardUniversitySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


# 특정 대학의 블로그 조회
class BoardUniversityDetail(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardUniversityDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        university = self.kwargs['university']
        queryset = Board.objects.filter(user__university=university)
        return queryset

    
# 특정 블로그 조회
class BoardDetail(RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]


# 특정 블로그 삭제
class BoardDetailDestroy(RetrieveDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]


# 특정 블로그 수정
class BoardDetailUpdate(RetrieveUpdateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]


# 댓글 조회
class CommentsList(ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post']
        queryset = Comments.objects.filter(post=post_id)
        return queryset


# 특정 댓글 조회
class CommentsDetail(RetrieveAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    lookup_url_kwarg = 'id'


# 댓글 삭제
class CommentsDestroy(RetrieveDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    lookup_url_kwarg = 'id'


# 댓글 수정
class CommentsUpdate(RetrieveUpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    lookup_url_kwarg = 'id'