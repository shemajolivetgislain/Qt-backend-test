from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse
from .models import Post, Comment
from .serializers import PostSerializer, ReadPostSerializer, CommentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class BlogCreateAPIView(APIView):
    """Blog post API view"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            title = request.data.get('title', None)
            if Post.objects.filter(title=title).exists():
                return Response(
                    {"error": "A blog with this title already exists."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            blog_serializer = PostSerializer(data=request.data)
            if blog_serializer.is_valid():
                blog_serializer.save(author=request.user)
                return Response(
                    {"message": "Blog created successfully", "data": blog_serializer.data},
                    status=status.HTTP_201_CREATED
                )

            return Response(blog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class BlogListAPIView(APIView):
    
    def get(self, request):
        try:
            blogs = Post.objects.all()
            if not blogs:
                return Response(
                    {"message": "You have no blogs."},
                    status=status.HTTP_200_OK
                )
            serializer = ReadPostSerializer(blogs, many=True)
            return JsonResponse(
                {"message": "Blogs retrieved successfully", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# View of Blog Details

class BlogDetailAPIView(APIView):
    
    def get(self, request, blog_id):
        try:
            blog = Post.objects.get(id=blog_id)
            post_serializer = PostSerializer(blog)
            
            # Fetch and serialize related comments
            comments = Comment.objects.filter(post=blog)
            comment_serializer = CommentSerializer(comments, many=True)
            
            response_data = {
                "message": "Blog retrieved successfully",
                "data": {
                    "post": post_serializer.data,
                    "comments": comment_serializer.data,
                }
            }
            return JsonResponse(response_data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response(
                {"error": "Blog not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class BlogDetailUpdateDeleteAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    
        
    def patch(self, request, blog_id):
        try:
            blog = Post.objects.get(id=blog_id)
            if blog.author != request.user:
                return Response(
                    {"error": "You are not authorized to update this blog."},
                    status=status.HTTP_403_FORBIDDEN
                )
            blog_serializer = PostSerializer(blog, data=request.data)
            if blog_serializer.is_valid():
                blog_serializer.save()
                return Response(
                    {"message": "Blog updated successfully", "data": blog_serializer.data},
                    status=status.HTTP_200_OK
                )
            return Response(blog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response(
                {"error": "Blog not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
    def delete(self, request, blog_id):
        try:
            blog = Post.objects.get(id=blog_id)
            if blog.author != request.user:
                return Response(
                    {"error": "You are not authorized to delete this blog."},
                    status=status.HTTP_403_FORBIDDEN
                )
            blog.delete()
            return Response(
                {"message": "Blog deleted successfully."},
                status=status.HTTP_200_OK
            )
        except Post.DoesNotExist:
            return Response(
                {"error": "Blog not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )