from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages

def unauthenticated_user(view_func):
    def func_wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return func_wrapper

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def func_wrapper(request, *args, **kwargs):
            
            groups = None
            if request.user.groups.exists():
                # get all group names in a list type.
                groups = request.user.groups.values_list('name', flat=True)
            
            for group in groups:
                
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse('You are not authorized!')

        return func_wrapper
        
    return decorator