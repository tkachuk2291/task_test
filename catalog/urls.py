from django.urls import path

from catalog.views import index, BookListView, LiteraryFormatListView, AuthorListView , book_detail_view,test_session_view

urlpatterns = [
    path("catalog/", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-formats-list"),
    path("book/", BookListView.as_view(), name="book-list"),
    path("book/<int:pk>/", book_detail_view, name="book-detail"),
    path("authors/", AuthorListView.as_view(), name="authors-list"),
    path("test-session/", test_session_view, name="session-view"),
]

app_name = "literary-formats"

