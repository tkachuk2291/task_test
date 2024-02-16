from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, Http404
from django.views import generic

from catalog.models import Book, Author, LiteraryFormat
from django.shortcuts import render


# def index(request: HttpRequest) -> HttpResponse:
#     num_books = Book.objects.count()
#     num_author = Author.objects.count()
#     num_literary = LiteraryFormat.objects.count()
#     context = {
#         "num_books": num_books,
#         "num_authors": num_author,
#         "num_literary": num_literary
#     }
#     return render(request, "catalog/index.html", context=context)


class LiteraryFormatListView(LoginRequiredMixin, generic.ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_formats_list.html"
    context_object_name = "all_formats"


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    queryset = Book.objects.select_related("format")
    paginate_by = 10


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    context_object_name = "all_authors"


# def literary_formats_list_view(request: HttpRequest) -> HttpResponse:
#     literary_formats_list = LiteraryFormat.objects.all()
#     context = {
#         "all_formats": literary_formats_list
#     }
#     return HttpResponse(render(request, "catalog/literary_formats_list.html", context=context))
@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    num_authors = Author.objects.count()
    num_books = Book.objects.count()
    num_literary = LiteraryFormat.objects.count()
    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_literary": num_literary,
        "num_visits": num_visits,
    }
    return render(request, "catalog/index.html", context=context)


@login_required
def book_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        book = Book.objects.get(id=pk)
    except:
        raise Http404("Book does not exist")
    context = {
        "book": book,
    }
    return render(request, "catalog/book_detail.html", context=context)


def test_session_view(request: HttpRequest) -> HttpResponse:
    request.session["book"] = "Test session Book"
    return HttpResponse(f"<h4>Session Book test:{request.session['book']}<h4>"
                        "<h1>Session test</h1>")
