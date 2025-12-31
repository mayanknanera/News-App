from .models import Article, Comment
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "articles/article_list.html"

    def get_queryset(self):
        return Article.objects.all().order_by('-date')  # latest first

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "articles/article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = (
            self.object.comment_set.select_related("author").all().order_by("-comment_date", "-id")
        )
        context["comment_form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = CommentForm(request.POST)

        if form.is_valid():
            Comment.objects.create(
                article=self.object,
                author=request.user,
                comment=form.cleaned_data['comment'],
            )
            return redirect('article_detail', pk=self.object.pk)

        return self.render_to_response(
            self.get_context_data(
                object=self.object,
                comment_form=form
            )
        )


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ("title", "body", "image",)
    template_name = "articles/article_edit.html"

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "articles/article_create.html"
    fields = ("title", "body",'image',)
    success_url = reverse_lazy("article_list")

    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
