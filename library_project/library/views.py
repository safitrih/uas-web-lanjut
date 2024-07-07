# library/views.py
from rest_framework import viewsets
from .models import Author, Book, Borrower
from .serializers import AuthorSerializer, BookSerializer, BorrowerSerializer
from django.shortcuts import render


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BorrowerViewSet(viewsets.ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

def api_overview(request):
    api_urls = {
        'Authors List': '/api/authors/',
        'Books List': '/api/books/',
        'Borrowers List': '/api/borrowers/',
    }
    return render(request, 'library/api_overview.html', {'api_urls': api_urls})
