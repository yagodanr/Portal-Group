from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView

from .models import Poll, Option


# Create your views here.
class PollListView(ListView):
    model = Poll
    context_object_name = 'polls'

class PollDetailView(DetailView):
    model = Poll
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:    
        context = super().get_context_data(**kwargs)
        
        total_voted = 0
        for o in context["poll"].options.all():
            total_voted += o.voted.all().count()
        
        if total_voted == 0:
            percentages = [0 for i in context["poll"].options.all()] 
        else:
            percentages = list()
            for o in context["poll"].options.all():
                percentages.append(int(o.voted.all().count()* 100 / total_voted)) 

        context["options"] = zip(context["poll"].options.all(), percentages)
        context["total_voted"] = total_voted
        
        return context

    def post(self, request, *args, **kwargs):
        opt = Option.objects.get(id=request.POST["option"])
        user = request.user
        
        poll = opt.poll
        for o in poll.options.all():
            if user in o.voted.all():
                o.voted.remove(user)
                break
        
        opt.voted.add(request.user)
        opt.save()
        
        return self.get(request)

class PollCreateView(CreateView):
    model = Poll
    fields = ("title", )
    
    RANGE = 8
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["range"] = range(self.RANGE)
        
        return context
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        poll = Poll(title=request.POST.get("title"))
        poll.save()
        
        for i in range(self.RANGE):
            if request.POST.get(f"{i}"):
                print(i, request.POST.get(f"{i}"))
                opt = Option(name=request.POST.get(f"{i}"), poll=poll)
                opt.save()
                
        return redirect("detail-poll", poll.id)
                

