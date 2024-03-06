from django.urls import path
from .views import BooksListAPIView , BookDetailView , \
      BookUpdateView , BookDeleteView , \
      BookSpecialView, BooksListCreateView, \
      ListAPIView, DetailAPIView, BookViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('router', BookViewSet, basename='books')

urlpatterns = [
    # Concreate class-based views urls
    path("books/", BooksListAPIView.as_view()),
    path("books/<int:pk>/", BookDetailView.as_view()),
    path("books/<int:pk>/update/", BookUpdateView.as_view()),
    path("books/<int:pk>/delete/", BookDeleteView.as_view()),
    # Generic views urls
    path("main/<int:pk>/", BookSpecialView.as_view()),
    path("main/", BooksListCreateView.as_view()),
    # APIView urls
    path("simple/", ListAPIView.as_view()),
    path("simple/<int:pk>/", DetailAPIView.as_view()),
]   

urlpatterns += router.urls