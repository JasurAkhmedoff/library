from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from .models import Book,Category,Subcategory,Comment
from .forms import BookSearchForm
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from .forms import CreateUserForm,LoginForm
from django.contrib import messages
from library import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout



 


# views.py


@login_required
def book_list(request):
    search_query = request.GET.get('search_query', '')  # Get the search query from the request
    books_list = Book.objects.filter(Q(title__icontains=search_query) | Q(author__icontains=search_query)).order_by("-publication_date")
    ordered_books_list = sorted(books_list, key=lambda x: x.title.lower().startswith(search_query.lower()) or x.author.lower().startswith(search_query.lower()), reverse=True)
    paginator = Paginator(books_list, 10)  # Show 10 books per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books/index.html', {'page_obj': page_obj, 'search_query': search_query})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    similar_books = Book.objects.filter(subcategory=book.subcategory).exclude(id=book.id)
   # Add this line for debugging
    return render(request, 'books/book_details.html', {'book': book, 'similar_books': similar_books})

# views.py# views.py
def book_search(request):
    query = request.GET.get('query')
    if query:
        results = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        results = Book.objects.all()
    return render(request, 'books/index.html', {'results': results, 'query': query})

def category_list(request):
    categories = Category.objects.all()

    categories_with_subcategories = {}

    for category in categories:
      
        subcategories = Subcategory.objects.filter(category=category)
     
        categories_with_subcategories[category] = subcategories

    return render(request, 'books/category_list.html', {"categories_with_subcategories": categories_with_subcategories})

def subcategory_books(request, subcategory_id):
    subcategory = get_object_or_404(Subcategory, id=subcategory_id)
    books = Book.objects.filter(subcategory=subcategory)
    return render(request, 'books/subcategory_books.html', {'subcategory': subcategory, 'books': books})



@login_required
def like_or_unlike(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.user in book.like.all():
        book.like.remove(request.user)
    else:
        book.like.add(request.user)
    return redirect('index')

def user_favourites(request):
    user_favourites = Book.objects.filter(like=request.user)
    return render(request, 'books/user_favourite.html', {'user_favourites': user_favourites})

@login_required
def already_read(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.user in book.already_read.all():
        book.already_read.remove(request.user)
    else:
        book.already_read.add(request.user)
    return redirect('index')

def already_read_books(request):
    already_read_books = Book.objects.filter(already_read=request.user)
    return render(request, 'books/already_read_books.html', {'already_read_books': already_read_books})


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')
        
        # Create a new user
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        
        # Registration successful, redirect to index
        messages.success(request, "Registration successful. You can now log in.")
        return redirect('index')  # Redirect to the 'index' page
    
    return render(request, 'books/register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        # Check if user authentication was successful
        if user is not None:
            # Log in the user
            auth_login(request, user)
            return redirect('index')  # Redirect to the desired page after login
        else:
            # Authentication failed
            messages.error(request, 'Invalid username or password.')
            return render(request, 'books/login.html')
    
    return render(request, 'books/login.html')



def logout(request):
  if request.method == 'POST':
      auth_logout(request)
      return redirect('index')  
  else:
      return render(request, 'books/logout.html')    
  

