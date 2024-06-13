from typing import Any
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
