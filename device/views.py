from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from .models import Device
from .serializers import WarningDevices
from .forms import DeviceForm
from django.shortcuts import redirect
from django.contrib import messages


def device_new(request):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save()
            device_name = form.cleaned_data.get('name')
            messages.success(request, f'Девайс {device_name} был успешно добавлен. ')
            return redirect('device_detail', pk=device.pk)
    else:
        form = DeviceForm()
    return render(request, 'device/device_edit.html', {'form': form})


class WarningDevicesViewSet(viewsets.ModelViewSet):
    serializer_class = WarningDevices
    queryset = Device.objects.all()


class ShowDeviceView(ListView):
    model = Device
    template_name = 'device/show.html'
    context_object_name = 'device'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ShowDeviceView, self).get_context_data(**kwargs)
        all_devices = Device.objects.all()
        type = self.request.GET.get('type')
        filter_devices_set = all_devices.filter(type=type)
        context['device_filter'] = filter_devices_set
        return context


class DeviceDetailView(DetailView):
    model = Device
    template_name = 'device/detail.html'


class CreateDeviceView(CreateView):
    model = Device
    fields = ['name', 'address', 'type', 'latitude', 'longitude', 'radius']
    template_name = 'device/device_form.html'


class UpdateDeviceView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Device
    fields = ['name', 'address','type','latitude','longitude','radius']

    # после нажатия на кнопку добавить-будет вызываться форм валид
    # в поле автору будем устанав опред значение
    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

    def test_func(self):
        device = self.get_object()
        if self.request.user == device.name:  # проверяем авторизованного пользователя и  автора статьи
            return True
        return False


class DeLeteDeviceView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Device
    success_url = reverse_lazy('show')

    def test_func(self):
        device = self.get_object()
        if self.request.user == device.name:  # проверяем авторизованного пользователя и  автора статьи
            return True
        return False
