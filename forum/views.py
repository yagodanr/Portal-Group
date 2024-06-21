from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Branch, Post

# Create your views here.

class BranchListView(ListView):
    model = Branch
    template_name = 'forum/branch-list.html'
    context_object_name = 'branches'

class BranchDetailView(DetailView):
    model = Branch
    template_name = 'forum/branch-detail.html'
    context_object_name = 'branch'

class BranchCreateView(CreateView):
    model = Branch
    fields = ("name", )
    template_name = 'forum/branch-create.html'

    def post(self, request, *args, **kwargs):
        branch = Branch(name=request.POST.get("name"), creator=request.user)
        branch.save()
                
        return redirect("branch-list")
    
class PostCreateView(CreateView):
    model = Post
    fields = ("name", "text")
    template_name = 'forum/post-create.html'

    def post(self, request, *args, **kwargs):
        _branch = get_object_or_404(Branch, pk=self.kwargs.get("pk"))
        _post = Post(name=request.POST.get("name"), text=request.POST.get("text"), author=request.user, branch=_branch)
        _post.save()
                
        return redirect("branch-detail", self.kwargs.get("pk"))
