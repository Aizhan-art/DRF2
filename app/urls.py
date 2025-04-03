from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.book_list_view),
    path('books/create/', views.book_create_view),
    path('books/partial/update/<int:book_id>/', views.book_partial_update_view),
    path('books/delete/<int:book_id>/', views.book_delete_view)
]