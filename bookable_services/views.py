from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Service


# Create your views here.
class ServiceListView(LoginRequiredMixin, ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'


# class ServiceList(View, LoginRequiredMixin):
#     model = Service
#     template_name = 'service_list.html'

#     def get(self, request, *args, **kwargs):
#         services = Service.objects.all()
#         return render(request, self.template_name, {'services': services})


# class SelectPlace(View):
#     select_place_page = 'book_service_place.html'

#     def get(self, request, service_id):
#         service = get_object_or_404(Service, id=service_id)
#         places = Place.objects.filter(slot__service=service).distinct()
#         for place in places:
#             slots = Slot.objects.filter(service=service, place=place)
#             place.total_available_slots = IndividualSlot.objects.filter(slot__in=slots, is_booked=False).count()
#         return render(request, self.select_place_page, {'service': service, 'places': places})

#     def post(self, request, *args, **kwargs):
#         service_id = request.POST.get('service_id')
#         place_id = request.POST.get('place_id')
#         print(f"SelectPlace POST: Service ID - {service_id}, Place ID - {place_id}")
#         return redirect('book_service', service_id=service_id, place_id=place_id)


# # class BookService(LoginRequiredMixin, View):
# #     model = Booking
# #     service_booking_page = 'book_service.html'

# #     def get(self, request, service_id, place_id):
# #         service = get_object_or_404(Service, id=service_id)
# #         place = get_object_or_404(Place, id=place_id)
# #         current_time = timezone.now()
# #         slots = Slot.objects.filter(service=service, place=place, start_time__gte=current_time)
# #         individual_slots = IndividualSlot.objects.filter(slot__in=slots, is_booked=False)
# #         print(f"Individual slots: {individual_slots}")
# #         return render(request, self.service_booking_page, {'form': form, 'individual_slots': individual_slots, 'service': service, 'place': place})

# #     def post(self, request, service_id, place_id):
# #         print("POST request data:", request.POST) 
# #         individual_slot_id = request.POST.get('individual_slot_id')
# #         print(f"POST request: Individual Slot ID - {individual_slot_id}")
# #         individual_slot = get_object_or_404(IndividualSlot, id=individual_slot_id)

# #         if not individual_slot.is_booked:
# #             individual_slot.is_booked = True
# #             individual_slot.save()
# #             new_booking = Booking.objects.create(
# #                 user=request.user,
# #                 individual_slot=individual_slot,
# #                 service=individual_slot.slot.service,
# #                 status='pending'
# #             )
# #             return redirect('book_service_confirmation', booking_id=new_booking.id)
# #         else:
# #             messages.error(request, 'This place is already booked.')
# #             return redirect('select_place', service_id=service_id)


# def get_available_slots(request, service_id, location_id):
#     try:
#         service = get_object_or_404(Service, pk=service_id)
#         slots = Slot.objects.filter(service=service, location_id=location_id)
#         available_individual_slots = IndividualSlot.objects.filter(slot__in=slots, is_booked=False)
#         formatted_slots = [{'id': ind_slot.id, 'display': str(ind_slot)} for ind_slot in available_individual_slots]
#         return JsonResponse({'slots': formatted_slots})
#     except Service.DoesNotExist:
#         return JsonResponse({'error': 'Service not found'}, status=404)


# # @login_required
# # def book_service_confirmation(request, booking_id):
# #     latest_booking = get_object_or_404(Booking, id=booking_id, user=request.user)
# #     return render(request, 'book_service_confirmation.html', {'booking': latest_booking})

# # @login_required
# # def booking_status(request):
# #     bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
# #     return render(request, 'booking_list.html', {'bookings': bookings})

# # @login_required
# # def cancel_booking(request, booking_id):
# #     booking = get_object_or_404(Booking, id=booking_id, user=request.user)
# #     if booking.status != 'cancelled':
# #         booking.status = 'cancelled'
# #         booking.individual_slot.is_booked = False
# #         booking.individual_slot.save()
# #         booking.save()
# #     else:
# #         messages.error(request, 'Booking cannot be cancelled.')
# #     return redirect('booking_status')
