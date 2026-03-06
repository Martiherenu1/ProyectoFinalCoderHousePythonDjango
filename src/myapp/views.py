from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Servicio
from datetime import datetime, time, timedelta
from .models import Turno
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from .forms import TurnoForm

@login_required
def index(request):
    datos = {
        "titulo" : "Django",
        "descripcion" : "Proyecto Final Python Django",
    }
    return render(request, "myapp/index.html", datos)


from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

class ServicioListView(LoginRequiredMixin, ListView):
    model = Servicio
    template_name = "myapp/servicio_list.html"


class ServicioCreateView(UserPassesTestMixin, CreateView):
    model = Servicio
    fields = "__all__"
    template_name = "myapp/servicio_form.html"
    success_url = reverse_lazy("lista_servicios")

    def test_func(self):
        return self.request.user.is_staff


class ServicioUpdateView(UserPassesTestMixin, UpdateView):
    model = Servicio
    fields = "__all__"
    template_name = "myapp/servicio_form.html"
    success_url = reverse_lazy("lista_servicios")

    def test_func(self):
        return self.request.user.is_staff


class ServicioDeleteView(UserPassesTestMixin, DeleteView):
    model = Servicio
    template_name = "myapp/servicio_confirm_delete.html"
    success_url = reverse_lazy("lista_servicios")

    def test_func(self):
        return self.request.user.is_staff

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myapp/register.html"
    success_url = reverse_lazy("login")

def generar_horarios_disponibles(fecha):

    dia_semana = fecha.weekday()

    # 0 = lunes
    # 6 = domingo

    if dia_semana == 0 or dia_semana == 6:
        return []

    if dia_semana == 5:  # sábado
        hora_inicio = time(10, 0)
        hora_fin = time(15, 0)
    else:
        hora_inicio = time(10, 0)
        hora_fin = time(18, 0)

    horarios = []

    hora_actual = datetime.combine(fecha, hora_inicio)

    while hora_actual.time() <= hora_fin:
        horarios.append(hora_actual.time())
        hora_actual += timedelta(minutes=30)

    # buscar turnos ocupados
    ocupados = Turno.objects.filter(fecha=fecha).values_list('hora', flat=True)

    disponibles = [h for h in horarios if h not in ocupados]

    return disponibles

class TurnoCreateView(LoginRequiredMixin, CreateView):
    model = Turno
    form_class = TurnoForm
    template_name = "myapp/turno_form.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.cliente = self.request.user

        try:
            form.instance.full_clean()
        except ValidationError as e:
            form.add_error(None, e)
            return self.form_invalid(form)

        return super().form_valid(form)

def get_horarios_disponibles(request):
    fecha_str = request.GET.get('fecha')
    if not fecha_str:
        return JsonResponse({'horarios': []})
    try:
        fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d').date()
    except ValueError:
        return JsonResponse({'horarios': []})
        
    disponibles = generar_horarios_disponibles(fecha_obj)
    horarios_str = [h.strftime('%H:%M') for h in disponibles]
    return JsonResponse({'horarios': horarios_str})
