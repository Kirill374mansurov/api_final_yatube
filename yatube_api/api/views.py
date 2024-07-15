from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import viewsets, permissions, mixins, filters
from rest_framework.pagination import LimitOffsetPagination

from .serializers import PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer
from posts.models import Post, Comment, Group, Follow, User
from .permissions import AuthorOrReadOnly


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        posts = get_object_or_404(Post, pk=post_id)
        new_queryset = posts.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        post=Post.objects.get(id=self.kwargs.get('post_id')))


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following',)
    queryset = Follow.objects.all()

    def get_queryset(self):
        username = self.request.user
        user = get_object_or_404(User, username=username)
        new_queryset = user.follows_user.all()
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
