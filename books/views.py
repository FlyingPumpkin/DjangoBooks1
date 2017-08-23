from django.shortcuts import render
from django.shortcuts import render_to_response
from requests import request
from books.models import Publisher, Author, Book


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains = q)
            return render_to_response('search_result.html', {'books': books, "query": q})
    return render_to_response('search_form.html', {'error': error})


