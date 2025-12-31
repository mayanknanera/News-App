from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from articles.models import Article

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("article_list")  # replace with your homepage URL

    def form_valid(self, form):
        # Save user
        response = super().form_valid(form)
        # Auto-login after signup
        login(self.request, self.object)
        return response