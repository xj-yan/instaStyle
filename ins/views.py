from annoying.decorators import ajax_request

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy, reverse

from ins.models import Post, InstaUser, Like
from ins.forms import CustomerUserCreationForm


# Create your views here.
class HelloWorld(TemplateView):
    template_name = 'test.html'


class PostsView(ListView):
    model = Post
    template_name = 'index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'
    login_url = 'login'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'

    def get_success_url(self):
        return reverse_lazy("posts")


class SignUp(CreateView):
    form_class = CustomerUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }
