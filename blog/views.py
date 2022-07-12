from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import  (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import QueryForm
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.

def query(request):
    if request.method == "POST" :
        form = QueryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your Query has been submitted!')
            # return redirect('')
    else:
        form = QueryForm
    return render(request, 'blog/query.html', {'form' : form})

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html',{'title' : 'About' })


