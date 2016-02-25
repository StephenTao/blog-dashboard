from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from horizon import exceptions
from horizon import forms
from horizon import messages

from blogdashboard import api


class UpdateForm(forms.SelfHandlingForm):
    title = forms.CharField(
        label=_("title"),
        required=False,
        widget=forms.TextInput()
    )

    content = forms.CharField(
        label=_("content"),
        required=False,
        widget=forms.widgets.Textarea()
    )


    def handle(self, request, data):
        try:

            ex = api.blogclient(request).blogs.update(data)

            msg = _('Execution has been created with id "%s".') % ex.id
            messages.success(request, msg)

            return True
        except Exception:
            msg = _('Failed to execute workflow "%s".') % data['title']
            redirect = reverse('horizon:blogs:blogs:index')
            exceptions.handle(request, msg, redirect=redirect)

class CreateForm(forms.SelfHandlingForm):
    title = forms.CharField(
        label=_("title"),
        required=False,
        widget=forms.TextInput()
    )

    content = forms.CharField(
        label=_("content"),
        required=False,
        widget=forms.widgets.Textarea()
    )


    def handle(self, request, data):
        try:

            ex = api.blogclient(request).blogs.create(data)

            msg = _('Execution has been created with id "%s".') % ex.id
            messages.success(request, msg)

            return True
        except Exception:
            msg = _('Failed to execute workflow "%s".') % data['title']
            redirect = reverse('horizon:blogs:blogs:index')
            exceptions.handle(request, msg, redirect=redirect)
