from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import User
from .forms import UserForm
from django.contrib.messages.views import SuccessMessageMixin
from main.decorators import unauthenticated_user
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import Http404


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.
        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()

        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(("No %(verbose_name)s found matching the query") %
                        {'verbose_name': queryset.model._meta.verbose_name})

        current_user = self.request.user

        if current_user != obj:
            raise PermissionDenied
        
        return obj

class UserCreate(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    success_url = "/accounts/login/"
    success_message = "Account was successfully created."

    @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
