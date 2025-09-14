from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseBadRequest
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Day, Seat, Worker

# Vista principal de asignaciones
class SeatListView(View):
    def get(self, request):
        days = Day.objects.prefetch_related('seats__worker').all().order_by('id')
        available_workers = Worker.objects.filter(seats__isnull=True)
        
        return render(request, 'schedule/seat_list.html', {
            'days': days,
            'workers': available_workers
        })

    def post(self, request):
        worker_id = request.POST.get('worker')
        seat_id = request.POST.get('seat')

        if not worker_id or not seat_id:
            messages.error(request, "Debe seleccionar un trabajador y un asiento")
            return redirect('schedule:seat_list')

        try:
            worker = Worker.objects.get(pk=worker_id)
            seat = Seat.objects.get(pk=seat_id)
            
            if worker.seats.exists():
                messages.error(request, "Este trabajador ya tiene un asiento asignado")
                return redirect('schedule:seat_list')
                
            if seat.worker is not None:
                messages.error(request, "Este asiento ya está ocupado")
                return redirect('schedule:seat_list')
                
            seat.worker = worker
            seat.save()
            messages.success(request, f"Asiento asignado correctamente a {worker.name}")
            
        except (Worker.DoesNotExist, Seat.DoesNotExist):
            messages.error(request, "Trabajador o asiento no válido")

        return redirect('schedule:seat_list')

# Vistas CRUD para trabajadores
class WorkerListView(ListView):
    model = Worker
    template_name = 'schedule/worker_list.html'
    context_object_name = 'workers'

class WorkerCreateView(CreateView):
    model = Worker
    template_name = 'schedule/worker_form.html'
    fields = ['name']
    success_url = reverse_lazy('schedule:worker_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Trabajador creado exitosamente')
        return super().form_valid(form)

class WorkerUpdateView(UpdateView):
    model = Worker
    template_name = 'schedule/worker_form.html'
    fields = ['name']
    success_url = reverse_lazy('schedule:worker_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Trabajador actualizado exitosamente')
        return super().form_valid(form)

class WorkerDeleteView(DeleteView):
    model = Worker
    template_name = 'schedule/worker_confirm_delete.html'
    success_url = reverse_lazy('schedule:worker_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Trabajador eliminado exitosamente')
        return super().delete(request, *args, **kwargs)

@require_POST
def reset_assignments(request):
    Seat.objects.all().update(worker=None)
    messages.success(request, "Todas las asignaciones han sido reiniciadas correctamente.")
    return redirect('schedule:seat_list')