from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Postear
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def listar_publicaciones(request):
    publicaciones = Postear.objects.filter(fecha_publicacion__lte = timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_publicaciones.html', {'publicaciones':publicaciones})

def detalle_publicacion(request,pk):
    publicacion = get_object_or_404(Postear,pk=pk)
    return render(request,'blog/detalle_publicacion.html',{'publicacion':publicacion})

def nueva_publicacion(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.detalle_publicacion', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/editar_publi.html', {'form': form})


def editar_publi(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.detalle_publicacion', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/editar_publi.html', {'form': form})
