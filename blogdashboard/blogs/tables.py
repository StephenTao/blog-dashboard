from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy

from horizon import tables
from blogdashboard import api


class UpdateBlog(tables.LinkAction):
    name = "Update"
    verbose_name = _("Update")
    url = "horizon:blogs:blogs:update"
    classes = ("ajax-modal", "btn-edit")

class DeleteBlog(tables.DeleteAction):
    @staticmethod
    def action_present(count):
        return ungettext_lazy(
            u"Delete Blog",
            u"Delete Blogs",
            count
        )

    @staticmethod
    def action_past(count):
        return ungettext_lazy(
            u"Deleted Blog",
            u"Deleted Blogs",
            count
        )

    def delete(self, request, obj_id):
        api.blogclient(request).blogs.delete(obj_id)


class CreateBlog(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Blog")
    url = "horizon:blogs:blogs:create"
    classes = ("ajax-modal",)
    icon = "plus"


class BlogFilterAction(tables.FilterAction):
    def filter(self, table, flavors, filter_string):
        """Really naive case-insensitive search."""
        q = filter_string.lower()

        def comp(flavor):
            return q in flavor.name.lower()

        return filter(comp, flavors)


class BlogsTable(tables.DataTable):
    title = tables.Column("title", verbose_name=_("Title"))
    content = tables.Column("content", verbose_name=_("Content"))
    id = tables.Column("id", verbose_name=_("ID"))

    def get_object_id(self, datum):
        return datum.title

    class Meta:
        name = "Blogs"
        verbose_name = _("Blogs")
        table_actions = (BlogFilterAction, CreateBlog, DeleteBlog)
        row_actions = (UpdateBlog,DeleteBlog)

