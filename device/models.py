from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Device(models.Model):
	DEVICE_TYPE = (
		(None, 'Выберите тип устройства'),
		('s', 'Сирена'),
        ('m', 'Громкоговоритель')
	)
	name = models.CharField("Название", max_length=200)
	address = models.CharField("Адрес", max_length=200)
	type = models.CharField( max_length=1, default='None', choices=DEVICE_TYPE,verbose_name='Тип')
	latitude = models.DecimalField(default="0.0",verbose_name='Широта', max_digits=10, decimal_places=6)
	longitude = models.DecimalField(default="0.0",verbose_name='Долгота', max_digits=10, decimal_places=6)
	radius = models.PositiveIntegerField(default="0.0",verbose_name='Радиус')



	def get_absolute_url(self):
		return reverse('device_detail', args=[str(self.id)])

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Устройства'
		verbose_name = 'Устройство'
		ordering = ['radius']
		unique_together = ('name', 'type','address')
