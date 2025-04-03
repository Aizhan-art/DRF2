from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Book
from .serializers import BookListSerializer, BookCreateSerializer, BookUpdateSerializer


@api_view(['GET'])
def book_list_view(request):
    books = Book.objects.all()
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def book_create_view(request):
    serializer = BookCreateSerializer(data=request.data, context={'request': request})
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def book_partial_update_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    serializer = BookUpdateSerializer(book, data=request.data, context={'request': request}, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def book_delete_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return Response({'message': 'Книга удалена'}, status=status.HTTP_204_NO_CONTENT)

