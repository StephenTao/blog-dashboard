
import json
import logging

from django import conf
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms
from horizon import tables
from horizon import tabs
from horizon import workflows

from blogdashboard import api
from blogdashboard.blogs.tables import BlogsTable
from blogdashboard.blogs import forms as blog_form


class IndexView(tables.DataTableView):
    table_class = BlogsTable
    template_name = 'blogs/blogs/index.html'

    def get_data(self):
        return api.blogclient(self.request).blogs.list()

class CreateView(forms.ModalFormView):
    form_class = blog_form.CreateForm
    template_name = 'blogs/blogs/create.html'
    page_title = _("Create Blog")
    success_url = reverse_lazy("horizon:blogs:blogs:index")

class UpdateView(forms.ModalFormView):

    form_class = blog_form.UpdateForm
    template_name = 'blogs/blogs/details.html'
    success_url = reverse_lazy("horizon:blogs:blogs:index")

    def get_context_data(self, **kwargs):
        content = super(UpdateView, self).get_context_data(**kwargs)

        content["title"] = self.kwargs['title']
        #context["context"] = self.kwargs['context']

        return content

    def get_initial(self, **kwargs):
        return {'title': self.kwargs['title']}