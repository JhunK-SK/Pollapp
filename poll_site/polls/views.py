from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Poll
from .forms import PollForm
from django.http import JsonResponse

def index(request):
    polls = Poll.objects.all().order_by('-created_date')
    
    paginator = Paginator(polls, 3)
    
    page = request.GET.get('page')
    
    polls = paginator.get_page(page)
    
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

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    
    if request.method == 'POST':
        selected_option = request.POST['poll-option']
        if selected_option == 'option_one':
            poll.option_one_count += 1
        elif selected_option == 'option_two':
            poll.option_two_count += 1
        elif selected_option == 'option_three':
            poll.option_three_count += 1
        else:
            return redirect('vote', poll.id)
        poll.save()
        return redirect('home')
        
    context = {'poll': poll}
    return render(request, 'polls/vote.html', context)

def result(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {'poll': poll}
    return render(request, 'polls/result.html', context)

def delete_poll(request, poll_id):
    poll = Poll.objects.get(pk=poll_id).delete() 
    return redirect('home')

def result_data(request, obj):
    voteData = []
    poll = Poll.objects.get(id=obj)
    
    voteData.append({
        poll.option_one: poll.option_one_count
    })
    voteData.append({
        poll.option_two: poll.option_two_count
    })
    voteData.append({
        poll.option_three: poll.option_three_count
    })
    return JsonResponse(voteData, safe=False)