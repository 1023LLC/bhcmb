# bands/views.py

from django.shortcuts import render
from django.views import View

from .models import Event




class HomeView(View):
    def get(self, request):
        # Assuming you have a template named 'home.html' in your 'bands/templates' directory
        return render(request, 'core/home.html')

class AboutView(View):
    def get(self, request):
        # You can customize this data based on what you want to display on the about page
        about_data = {
            'about_header': 'About Us',
            'testimonial_text': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid corrupti eaque excepturi itaque. Officia omnis, distinctio fugit similique facilis accusantium iusto odio pariatur aperiam dolor reprehenderit doloremque obcaecati corrupti magnam minima adipisci quo unde eos praesentium explicabo earum maiores. Nam exercitationem ab fuga non nobis, soluta alias quaerat harum minima!',
            'image_url': './7365164.jpg',
        }
        return render(request, 'bands/about.html', {'about_data': about_data})

class EventsView(View):
    def get(self, request):
        events_data = Event.objects.all()
        return render(request, 'core/events.html', {'events_data': events_data})
