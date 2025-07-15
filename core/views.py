from rest_framework import viewsets
from .models import NewPost
from .serializers import NewPostSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from drf_spectacular.utils import extend_schema

@extend_schema(
    description='Publications handle API. Requires authentication.',
    tags=['Publications'],
)
class NewPostViewSet(viewsets.ModelViewSet):
    queryset = NewPost.objects.all()
    serializer_class = NewPostSerializer

    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title'] 

@extend_schema(
    description='Register account to receive JWT Token',
    tags=['Registration'],
)
class RegisterApiView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]