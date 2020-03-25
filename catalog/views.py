from django.db.models import Q
from django.views.generic import ListView
from .models import Car


class CarList(ListView):
    model = Car
    template_name = 'list.html'
    context_object_name = 'cars'

    def get_queryset(self):

        search_query = self.request.GET.get('search', '')
        result = Car.objects.all()
        if search_query:
            result = Car.objects.filter(Q(brand__name__icontains=search_query)
                                        | Q(model_of_car__icontains=search_query)
                                        | Q(year__contains=search_query)
                                        | Q(transmission__icontains=Car.transmission_choice(search_query))
                                        | Q(color__name__icontains=search_query))
        return result
