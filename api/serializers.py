

from rest_framework.serializers import ModelSerializer

from base.models import (
    User,
)
from web.models import (
    Category,
    Tag,
    Post,
    Comment,
)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'