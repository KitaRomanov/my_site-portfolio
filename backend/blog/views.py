
from django.views.generic.list import ListView

from blog.models import Publication
from common.views import TitleMixin


class BlogListView(TitleMixin, ListView):
    model = Publication
    template_name = 'blog/blog.html'
    title = 'Кулинарный блог'

    def get_queryset(self):
        queryset = super(BlogListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset
