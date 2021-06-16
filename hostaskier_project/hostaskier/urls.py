from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('host-form/', views.HostFormView.as_view(template_name='hostaskier/host_form.html'), name='hostform'),
    path('skier-form/', views.SkierFormView.as_view(template_name='hostaskier/skier_form.html'), name='skierform'),
]
