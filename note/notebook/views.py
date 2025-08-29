from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, CreateNoteForm
from .models import Note
from django.views import generic
from django.contrib.auth.views import LoginView


# Create your views here.

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    initial = {'key': 'value'}
    template_name = 'signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')
        return super(SignUpView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect(to='notebook:login')
        return render(request, self.template_name, {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        return super(CustomLoginView, self).form_valid(form)


class CreateNoteView(generic.CreateView):
    form_class = CreateNoteForm
    model = Note
    template_name = 'note_form.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('notebook:login')

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})


class ListNoteView(generic.ListView):
    model = Note
    template_name = 'list_note.html'
    context_object_name = 'notes'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(to='notebook:login')

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)


class UpdateNoteView(generic.UpdateView):
    model = Note
    form_class = CreateNoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('notebook:list_note')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('notebook:login')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)


class DeleteNoteView(generic.DeleteView):
    model = Note
    template_name = 'note_confirm_delete.html'
    success_url = reverse_lazy('notebook:list_note')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('notebook:login')

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)
