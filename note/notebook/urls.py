from django.urls import path
from .views import SignUpView, ListNoteView, CustomLoginView, CreateNoteView, UpdateNoteView, DeleteNoteView
from django.contrib.auth.views import LogoutView

app_name = 'notebook'

urlpatterns = [
    path('', ListNoteView.as_view(), name='list_note'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='notebook:login'), name='logout'),
    path('note/create/', CreateNoteView.as_view(), name='create_note'),
    path('note/<int:pk>/update', UpdateNoteView.as_view(), name='update_note'),
    path('note/<int:pk>/delete', DeleteNoteView.as_view(), name='delete_note')
]