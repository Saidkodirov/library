from django.urls import path
from .views import BooksListAPIView , BookDetailView , \
      BookUpdateView , BookDeleteView , \
      BookSpecialView, BooksListCreateView, \
      ListAPIView, DetailAPIView, BookViewSet

from rest_framework.routers import SimpleRouter
from django.views.decorators.csrf import csrf_exempt

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
    path("simple/", csrf_exempt(ListAPIView.as_view())),
    path("simple/<int:pk>/", csrf_exempt(DetailAPIView.as_view())),
]   

urlpatterns += router.urls