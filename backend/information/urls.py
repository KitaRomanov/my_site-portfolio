from django.urls import path

from information.views import ContactView, ProjectsView, StackView

app_name = 'information'

urlpatterns = [
    path('contact', ContactView.as_view(), name='contact'),
    path('stack', StackView.as_view(), name='stack'),
    path('projects', ProjectsView.as_view(), name='projects')

]
