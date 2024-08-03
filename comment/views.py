from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blogs.models import Post, Comment
from blogs.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class CommentCreateAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            data = request.data.copy()
            data['post'] = post_id
            data['author'] = request.user.id

            serializer = CommentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Comment created Successful", "data": serializer.data,}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CommentListAPIView(APIView):
    def get(self, request, post_id):
        try:
            comments = Comment.objects.filter(post_id=post_id)
            serializer = CommentSerializer(comments, many=True)
            return Response({"message": "Blog comments Retrieved successful", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CommentDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id, author=request.user)
            serializer = CommentSerializer(comment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id, author=request.user)
            comment.delete()
            return Response({"message": "Comment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
