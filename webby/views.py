
from email.mime import image
from urllib import request
from django.urls import reverse_lazy 
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.http  import HttpResponse
from .models import Post
from django.contrib.auth.models import User
# Create your views here.


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by: int = 5

class UserPostListView(ListView):
    model = Post
    template_name: str = 'webby/user_post.html'
    context_object_name = "posts"
  
    paginate_by: int = 5
   
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')
   

class PostDetailView(DetailView):
    model = Post



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('webby-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

   


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




def about(request):
    posts = Post.objects.all()
    context ={
        'posts': posts
    }

    return render(request,'webby/about.html', context)



#     from django.core.paginator import Paginator 
# >>> posts =['1', '2','3', '4','5']  
# >>> p = Paginator(posts,2)
# >>> p.num_pages
# 3
# >>> for page in p.page_range:
# ...      print(page) 
# ... 
# 1
# 2
# 3
# >>> p1 = p.page(1)
# >>>
# >>> p1
# <Page 1 of 3>
# >>> p1.number
# 1
# >>> p1.object_list
# ['1', '2']

# p1.has_previous()
# False
# >>> p1.has_next()
# True
# >>> p1.next_page_number()
# 2
# >>>

#/?page=2  the question mark is a sign to tell the browser that you are about to add a parameter.