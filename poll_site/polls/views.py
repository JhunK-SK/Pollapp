from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Poll
from .forms import PollForm, CreateUserForm
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group

@unauthenticated_user
def register(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name='plain user')
            user.groups.add(group)
            
            messages.success(request, 'Account was created for ' + username)
            
            return redirect('login')
    
    context = {'form': form}
    return render(request, 'polls/register.html', context)

@unauthenticated_user
def loginPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('login')
        
    context = {}
    return render(request, 'polls/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def index(request):
    # print(list(request.user.groups.values_list('name', flat=True)))
    polls = Poll.objects.all().order_by('-created_date')
    
    paginator = Paginator(polls, 3)
    
    page = request.GET.get('page')
    
    polls = paginator.get_page(page)
    
    context = {'polls': polls}
    return render(request, 'polls/index.html', context)

@login_required(login_url='login')
def create(request):
    form = PollForm()
    
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    
    context = {'form': form}
    return render(request, 'polls/create.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def result(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {'poll': poll}
    return render(request, 'polls/result.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_poll(request, poll_id):
    poll = Poll.objects.get(pk=poll_id).delete() 
    return redirect('home')
