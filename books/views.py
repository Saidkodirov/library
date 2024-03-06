from .serializers import BookSerializer
from .models import Books
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from rest_framework.views import APIView
# Create your views here.

from rest_framework.viewsets import ModelViewSet

class BookViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

# * APIView API Views
class ListAPIView(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request):
        try:
            books = Books.objects.all()
            serializer_class = BookSerializer(books, many=True).data
            data = {
                "status": True,
                "books": serializer_class
            }
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            data = {
                "status": False,
                "message": "An error occured. Please try again !. Maybe there is no data in database."
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    @method_decorator(csrf_exempt)
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()
            data = {
                "status": True,
                "book": serializer.data
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "status": False,
                "message": "Your data is not valid. Serializer error !"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
            
class DetailAPIView(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request, pk):
        try:
            book = Books.objects.get(pk=pk)
            serializer = BookSerializer(book).data
            data = {
                "status": True,
                "book": serializer
            }
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            data = {
                "status": False,
                "message": "The books is not found with the given pk." 
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    @method_decorator(csrf_exempt)
    def patch(self, request,pk):
        book = Books.objects.get(pk=pk)
        serializer_class = BookSerializer(book, data=request.data, partial=True)
        if serializer_class.is_valid():
            book = serializer_class.save()
            data = {
                "status": True,
                "book": serializer_class.data
            }
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data = {
                "status": False,
                "message": "The given data is not valid. Serializer ERROR."
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    @method_decorator(csrf_exempt)
    def delete(self, request,pk):
        try:
            book = Books.objects.get(pk=pk)
            book.delete()
            data = {
                "status": True,
                "message": "Successfully deleted"
            }
            return Response(data=data , status=status.HTTP_204_NO_CONTENT)
        except:
            data = {
                "status": False,
                "message": "No content found with the given pk."
            }
            return Response(data=data , status=status.HTTP_404_NOT_FOUND)



# * Concreate API Views
class BooksListAPIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

#* GENERIC API VIEWS

class BookSpecialView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BooksListCreateView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer