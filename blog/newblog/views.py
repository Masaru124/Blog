from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

class home(ListView): 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_menu'] = Category.objects.all()
        return context
    model = Post
    template_name = 'home.html'

class articledetail(DetailView):

    model = Post
    template_name = 'articles_details.html' 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_menu'] = Category.objects.all()
        stuff=get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True

        context["total_likes"] =total_likes
        context["liked"]=liked
        return context

class addpost(CreateView):
    model = Post
    form_class = Postform
    template_name = 'add_posts.html'
    
class Updatepost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields=['title','body']
class deletepost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategory(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields= '__all__'

def CategoryView(request,cats):
    Category_posts = Post.objects.filter(category=cats)
    return render(request ,'categories.html',{'cats': cats, 'category_posts': Category_posts})

def Like(request,pk):
    post = get_object_or_404(Post, id=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
     post.likes.remove(request.user)
     liked=False
    else:
     post.likes.add(request.user )
     liked=True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
    

