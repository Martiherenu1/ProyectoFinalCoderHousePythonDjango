from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView
from .views import TurnoCreateView, get_horarios_disponibles
from .views import (
    index,
    ServicioListView,
    ServicioCreateView,
    ServicioUpdateView,
    ServicioDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("servicios/", ServicioListView.as_view(), name="lista_servicios"),
    path("servicios/crear/", ServicioCreateView.as_view(), name="crear_servicio"),
    path("servicios/<int:pk>/editar/", ServicioUpdateView.as_view(), name="editar_servicio"),
    path("servicios/<int:pk>/eliminar/", ServicioDeleteView.as_view(), name="eliminar_servicio"),

    path("login/", auth_views.LoginView.as_view(template_name="myapp/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),

    path("turno/nuevo/", TurnoCreateView.as_view(), name="crear_turno"),
    path("turno/horarios-disponibles/", get_horarios_disponibles, name="horarios_disponibles"),

]