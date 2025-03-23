from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser

from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth import logout

from .api.serializer import ChangeEmailSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post , Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.db.models import Q

from django.contrib.auth.decorators import login_required
# Create your views here.

    


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('profile')
       
            
    else:
        form = CustomUserCreationForm()
    return render(request,'blog/register.html', {'form' : form})

def profile_view(request):
    return render(request,'blog/profile.html')

def home_view(request):
    return render (render,'blog/home.html')

  
# def post_view(request):
#     return render(request,'blog/post.html')  

def custom_logout(request):
    logout(request)
    return redirect('logout_success')

def logout_success_view(request):
    return render(request,'blog/logs.html')   

  
class ChangeEmailView(generics.UpdateAPIView):
    serializer_class = ChangeEmailSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
class PostListView(ListView):
    model = Post
    template_name = "blog/list.html"
    queryset = Post.objects.all().order_by('-created_at')
    context_object_name = "posts"
    
    
class PostDetailView(DetailView):
    model = Post
    template_name ="blog/post_detail.html"
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments']= Comment.objects.filter(post=self.object).order_by('-created_at')
        return context

    
    # def post(self, request, *args, **kwargs):
    #     self.object=self.get_object()
    #     if request.user.is_authenticated:
    #         form = CommentForm(request.POST)
    #         if form.is_valid():
    #             comment = form.save(commit=False)
    #             comment.post = self.object
    #             comment.author = request.user   
    #             comment.save()
    #             return redirect('post_detail', pk=self.object.pk)
    #         else:
    #             print(form.errors)  # Debug invalid form errors
    #             return self.get(request, *args, **kwargs)
    #     else:
    #         return redirect('login')
                
    
    
    

    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/CreateView.html"
    #success_url = reverse_lazy('post_detail', pk = self.object.pk )
   # return redirect('detail_view', )
    
    def form_valid(self, form):
        self.object = self.get_object
        form.instance.author = self.request.user
        post = form.save()  # Save the post
        #return super().form_valid(form)
        return redirect('post_detail', pk=post.pk)
        

   

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/UpdateView.html"
    success_url = reverse_lazy("all_post")
    #test_func is for userpassestestmixim
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy('all_post')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
  
  
# class CommentView(ListView):
#     model = Comment
#     template_name = "blog/viewing.html"
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_edit.html"
    
    def test_func(self):
        Comment = self.get_object()
        return self.request.user == Comment.author
    
    def form_valid(self, form): 
        
        form.save()
        return redirect('post_detail', pk=self.object.post.pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] =self.get_object().post
        return context
    
    
    #view for handling delete comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/commentdelete.html"
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] =self.get_object().post
        return context
        
    def get_success_url(self):
        comment = self.get_object()
        return reverse_lazy("post_detail", kwargs = {'pk': comment.post.pk})
    

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name= "blog/comment_create.html"
    context_object_name = "comments"
        
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        post = get_object_or_404(Post, pk = self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    def get_success_url(self):
        return  reverse_lazy('post_detail', kwargs= {'pk': self.object.post.pk})
    
        
def search_posts(request):
    query = request.GET.get('q', '')
    results =[]

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)|
            Q(tags__name__icontains=query)
        ).distinct()    
    return render(request,'blog/search_results.html', {'query' : query, 'results' : results})

    


    
    
    
class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_by_tag.html'  # The template to display the posts for a specific tag
    context_object_name = 'posts'  # The variable name to use in the template for the list of posts

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']  # Get the slug from the URL
        tag = get_object_or_404(Tag, slug=tag_slug)  # Fetch the tag or 404 if not found
        return Post.objects.filter(tags=tag)  # Filter posts by the selected tag

