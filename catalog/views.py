from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Language
from django.views import generic


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a'
        ).count()
    num_authors = Author.objects.count() # method all() by default
    num_genres = Genre.objects.count()
    num_languages = Language.objects.count()

    # number of visits to this view, as counted in the session variable
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'index.html', {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_languages': num_languages,
        'num_visits': num_visits,
    })


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author
