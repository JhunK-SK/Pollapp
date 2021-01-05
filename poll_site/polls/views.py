from django.shortcuts import render, redirect
from .models import Poll
from .forms import PollForm

def index(request):
    polls = Poll.objects.all().order_by('-created_date')
    
    context = {'polls': polls}
    return render(request, 'polls/index.html', context)

def create(request):
    form = PollForm()
    
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    
    context = {'form': form}
    return render(request, 'polls/create.html', context)