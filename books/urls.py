from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name="index"),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('search/', views.book_search, name='book_search'),
    path('category_list/', views.category_list, name="category_list"),
    path('category_list/<int:subcategory_id>/', views.subcategory_books, name='subcategory_books'),
    path('user/favourites/', views.user_favourites, name='user_favourites'),
    path('book/<int:book_id>/like/', views.like_or_unlike, name='like_or_unlike'),  # Changed URL pattern
    path('user/already_read/', views.already_read_books, name='already_read_books'),
    path('book/<int:book_id>/already_read/', views.already_read, name='already_read'),  # 
    path('login/', views.login, name='login'),    # Login page
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]

