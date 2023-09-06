from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from base.models import (
    User,
)
from web.models import (
    Category,
    Tag,
    Post,
    Comment,
)
from .serializers import (
    UserSerializer,
    CategorySerializer,
    TagSerializer,
    PostSerializer,
    CommentSerializer,
)


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()