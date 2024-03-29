from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# do image
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import ImgForm

class Image(TemplateView):
    form = ImgForm
    template_name = 'blog/image.html'

    def post(self, request, *args, **kwargs):
        '''przesyła obraz'''
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()

            return HttpResponseRedirect(reverse_lazy('image_display', kwargs={'pk': obj.id}))
        
        context = self.get_context_data(form=form)
        return self.render_to_response(context)
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    

class ImageDisplay(DetailView):
    model = Post
    template_name = 'blog/image_display.html'
    context_object_name = 'image'


def post_list(request):
    posts = Post.objects.all()

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk) # jak nie znajdzie, zwróci 404

    return render(request, 'blog/post_detail.html', {'post': post})

def error_404_view(request, exception):
    data = {'name': "Blog dla programistów"}

    return render(request, 'blog/404.html', data)