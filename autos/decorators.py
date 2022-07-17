from functools import wraps
from django.http import HttpResponseRedirect


def admin_zone(view_func):
    def _decorator(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('home')  # If the user is not an admint, return him where you want...

    return wraps(view_func)(_decorator)
