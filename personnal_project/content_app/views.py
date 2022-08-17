from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView
from .models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'content_app/homepage.html'
    paginate_by= 5

    class Meta:
        ordering = ['id']

class PostCreateView(CreateView):
    model = Post
    fields = ['title','content', 'photo']
    template_name = 'content_app/create-blog.html'

    

    


