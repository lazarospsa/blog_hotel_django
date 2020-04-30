from django.shortcuts import render
from blog.models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#LoginRequiredMixin gia na checkarw an autos pou 9elei na kanei edit h' create ena post einai sundedemenos gia na sundiastei me to CreateView
#UserPassesTestMixin gia na checkarei ean o sugkekrimenos xrhsths ekane to post kai na mhn mporw egw na kanw edit allounou post
from django.shortcuts import get_object_or_404

#views is the file that controls the urls - views of my app

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    #<app>/<model>_<viewtype>.html <- auto psaxnei alla gia na to orisoume emeis diko mas template kanw template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # ta ta3inomei prwta einai auta p grapsame pio prosfata (automata me to onoma ordering)
    #edw 9a valoume paginator (selidopoihsh)
    paginate_by = 5

#for profile
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    #<app>/<model>_<viewtype>.html <- auto psaxnei alla gia na to orisoume emeis diko mas template kanw template_name = 'blog/home.html'
    context_object_name = 'posts'
    #edw 9a valoume paginator (selidopoihsh)
    paginate_by = 5

    def get_queryset(self): #if user exists
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        # ths formas o author = o user opou esteile to aithma (request)
        #running the form valid method, said the author befor send the form
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        # ths formas o author = o user opou esteile to aithma (request)
        #running the form valid method, said the author befor send the form
        return super().form_valid(form)

    def test_func(self):#UserPassesTestMixin to test_func einai apo edw
        post = self.get_object() #vazoume to post se mia metavlhth
        if self.request.user == post.author: #elegxoume ean o user p ekane to request einai idios me ton author tou post mas
            return True #ean einai ontws epistrefei true ara to epitrepei na ginei edit
        return False #eidallws aporhptetai

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = f'/blog' #success_url einai proka9orismeno tou django

    def test_func(self):#UserPassesTestMixin to test_func einai apo edw
        post = self.get_object() #vazoume to post se mia metavlhth
        if self.request.user == post.author: #elegxoume ean o user p ekane to request einai idios me ton author tou post mas
            return True #ean einai ontws epistrefei true ara to diagrafei
        return False #eidallws aporhptetai

def about(request):
    return render(request, 'blog/about.html')