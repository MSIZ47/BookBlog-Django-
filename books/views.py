from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# we use mixins in classed based view,for method based view we should use decorators
from django.contrib.auth.decorators import login_required

from books.forms import BookForm, CommentForm
from books.models import Book


class BookListView(ListView):
    def get_queryset(self):
        return Book.objects.all()

    template_name = 'books/book_list.html'
    paginate_by = 4
    context_object_name = 'books'


# we use @login_required decorator so that for seeing the detail of a book client must be login
@login_required
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comments = book.comment_set.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():  # if form is valid we don't save it immediately because client is only posting text
            comment = comment_form.save(commit=False)  # of a comment through form, so we save it but we don't commit it
            comment.book = book  # to the database until we assign book and user of the comment;then save it.
            comment.user = request.user  # [request.user] is the phrase from django that we use to take the user of
            # the comment
            comment.save()
            comment_form = CommentForm()  # we write this line so that after a comment saved the form in page gets clear
    else:
        comment_form = CommentForm()

    return render(request, 'books/book_detail.html',
                  {'book': book,
                   'comments': book_comments,
                   'form': comment_form,
                   })

def createnewbook(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST, request.FILES)
        if book_form.is_valid():
            form = book_form.save(commit=False)
            form.user = request.user
            form.save()
            book_form = BookForm()
            return redirect('book_list')
    else:
        book_form = BookForm()
    return render(request, 'books/book_create.html', {'form':book_form,})
    

# # we use LoginRequiredMixin so that client should be login for creating a book
# class BookCreateView(LoginRequiredMixin, CreateView):
#     model = Book
#     fields = ['title', 'author', 'description', 'price', 'image', ]
#     template_name = 'books/book_create.html'

# we use 'UserPassesTestMixin' so that only the user of each book can update or delete that book
# hint: we should always overwrite the 'test_func' when we use 'UserPassesTestMixin'
# and this method will handle the permission for us.


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'image', ]
    template_name = 'books/book_update.html'

    def test_func(self):
        obj = self.get_object()  # with 'get_object()' phrase of django we can get the book we are updating or deleting
        return obj.user == self.request.user # with this line we check if the user of a book is
        # the same with the user that is updating a book,otherwise it will through an exception


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

    def test_func(self):
        book = self.get_object()  # with 'get_object()' phrase of django we can get the book we are updating or deleting
        return book.user == self.request.user  # with this line we check if the user of a book is
        # the same with the user that is updating a book,otherwise it will through an exception
