from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Content
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .filters import ContentFilter


def Search(request):
    contents = Content.objects.all()
    myFilter = ContentFilter()

    return render(request, 'appcms/search.html', {'myFilter': myFilter})


def ContentListView(request):
    contents = Content.objects.order_by('date_posted')
    myFilter = ContentFilter(request.GET, queryset=contents)

    return render(request, 'appcms/homes.html', {'contents': contents, 'myFilter': myFilter})


class ContentDetailView(DetailView):
    model = Content
    template_name = 'appcms/content_detail.html'
    context_object_name = 'content'


class ContentCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Content
    fields = ['title', 'body', 'summary', 'category', 'pdf']
    success_url = reverse_lazy('home')
    template_name = 'appcms/postCreate.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ContentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/login/'
    model = Content
    fields = ['title', 'body', 'summary', 'pdf']
    template_name = 'appcms/postCreate.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        content = self.get_object()
        if self.request.user == content.author:
            return True
        return False


class ContentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Content
    template_name = 'appcms/contentDelete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
