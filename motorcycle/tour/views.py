from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from motorcycle.rent.forms import ContactUsForm
from motorcycle.rent.models import ContactUs
from motorcycle.tour.models import Tour, TourImage


# Create your views here.
class TourView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'tour/tour.html'

    def get_success_url(self):
        return reverse('tour-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tours'] = Tour.objects.all()
        return context


class SpecTourView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'tour/spec_tour_rent.html'

    def get_success_url(self):
        return reverse('tour-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_tour = Tour.objects.get(pk=self.kwargs.get('pk'))
        context['current_tour'] = current_tour
        return context
