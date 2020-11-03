from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from myApp.models import Post
from accounts.models import Account
from myApp.forms import CreatePostForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime


class AboutView(LoginRequiredMixin, TemplateView):
    template_name = 'myApp/about.html'


@login_required()
def homeView(request):
    return redirect('myApp:mytodo_list')


@login_required()
def createPostView(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('myApp:mytodo_list')

    else:
        form = CreatePostForm()

    return render(request, 'myApp/postForm.html', {'form': form})


@login_required()
def listPostView(request):
    user = request.user
    post_instance = Post.objects.filter(author=user.id, completion_status=False)

    paginator = Paginator(post_instance, 5)
    page = request.GET.get('page')
    try:
        post_instance = paginator.page(page)
    except PageNotAnInteger:
        post_instance = paginator.page(1)
    except EmptyPage:
        post_instance = paginator.page(paginator.num_pages)

    return render(request, 'myApp/postList.html', {'posts': post_instance, 'page': page})


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'postDetails'
    template_name = 'myApp/postDetail.html'


class PostCompletedDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'postDetails'
    template_name = 'myApp/postCompletedDetail.html'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    context_object_name = "post_delete"
    model = Post
    success_url = reverse_lazy('myApp:mytodo_list')
    template_name = 'myApp/postDelete.html'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'post', 'post_type']
    template_name = 'myApp/postUpdate.html'


@login_required()
def listPostCompletedView(request):
    user = request.user
    post_instance = Post.objects.filter(author=user.id, completion_status=True)

    paginator = Paginator(post_instance, 5)
    page = request.GET.get('page')
    try:
        post_instance = paginator.page(page)
    except PageNotAnInteger:
        post_instance = paginator.page(1)
    except EmptyPage:
        post_instance = paginator.page(paginator.num_pages)

    return render(request, 'myApp/postCompleted.html', {'posts': post_instance, 'page': page})


@login_required()
def listCompleteView(request, pk):
    post_instance = Post.objects.get(pk=pk)
    user = request.user
    requested_user = user.email
    actual_user = post_instance.author.email

    if request.method == 'POST':
        if requested_user == actual_user:
            post_instance.completion_status = True
            post_instance.save()
            print("authorized")
            return redirect('myApp:mytodo_completed')
        else:
            print("unauthorized")
            return redirect('myApp:mytodo_list')

    else:
        return render(request, 'myApp/savePostAsCompleted.html', {'post': post_instance})


@login_required()
def showWarningsView(request):
    user = request.user
    current_date = datetime.date.today()
    time_delta = datetime.timedelta(days=7)
    margin_date = current_date - time_delta
    post_instance = Post.objects.filter(author=user.id, completion_status=False, modified_date__lte=margin_date)

    paginator = Paginator(post_instance, 5)
    page = request.GET.get('page')
    try:
        post_instance = paginator.page(page)
    except PageNotAnInteger:
        post_instance = paginator.page(1)
    except EmptyPage:
        post_instance = paginator.page(paginator.num_pages)

    return render(request, 'myApp/warnings.html', {'posts': post_instance, 'page': page})
