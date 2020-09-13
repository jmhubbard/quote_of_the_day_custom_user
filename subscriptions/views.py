from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import UpdateView
from .models import Subscription
from .forms import SubscriptionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.forms import ValidationError
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
# from.django.core.urlresolvers import reverse_lazy

@login_required()
def subscription(request):
    current_user = request.user
    subscriptions = Subscription.objects.filter(user = current_user)
    context ={
        'current_user': current_user,
        'subscriptions': subscriptions
    }

    return render(request, 'subscriptions/subform.html', context)


class SubscriptionUpdate(LoginRequiredMixin, UpdateView):
    model = Subscription
    fields = ['is_subscribed',]
    template_name_suffix = '_update_form'

    
    def get_success_url(self):
        return reverse('subscription')


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
            raise Http404(_("No %(verbose_name)s found matching the query") %
                        {'verbose_name': queryset.model._meta.verbose_name})

        current_user = self.request.user

        if current_user != obj.user:
            raise PermissionDenied
        
        return obj




