from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Time(models.Model):
    time = models.TimeField(verbose_name="Время")

    def __str__(self):
        return f"{self.time}"

    class Meta:
        verbose_name = 'Время'
        verbose_name_plural = 'Время'


class Master(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    photo = models.FileField(upload_to='masters_photo/', verbose_name="Фото",
                             validators=[FileExtensionValidator(['svg', 'png', 'jpeg'])])
    description = models.TextField(verbose_name="Описание")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


class Date(models.Model):
    date = models.DateField(verbose_name="Дата")

    def __str__(self):
        return f"{self.date}"

    class Meta:
        verbose_name = 'Дата'
        verbose_name_plural = 'Даты'


class PreOrder(models.Model):
    reserved_time = models.TimeField(verbose_name="Время брони", null=True)
    reserved_date = models.TextField(verbose_name="Дата брони", null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    master = models.TextField(verbose_name="Мастер")  # внешний ключ

    def __str__(self):
        return str(self.reserved_time)[:19]

    class Meta:
        verbose_name = 'Предзаказ'
        verbose_name_plural = 'Предзаказы'


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание")
    short_description = models.TextField(verbose_name="Короткое описание", null=True)
    photo = models.FileField(upload_to='services_photo/', verbose_name="Фото",
                             validators=[FileExtensionValidator(['svg', 'png', 'jpeg'])])
    price = models.IntegerField(verbose_name="Цена услуги", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Order(models.Model):
    finish_time = models.DateTimeField(auto_now=True, verbose_name="Время завершения заказа")
    total_price = models.IntegerField(verbose_name="Общая стоимость", null=True)
    master_id = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Мастер")  # внешний ключ
    services = models.ManyToManyField(Service, verbose_name="Список услуг")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", null=True)

    def save(self, *args, **kwargs):
        tp = 0
        if self.pk is None:
            super(Order, self).save(*args, **kwargs)
        print(self.services.all())
        for service in self.services.all():
            tp += service.price
        self.total_price = tp
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"{str(self.finish_time)[:19]} {self.master_id.name} {self.master_id.surname}"

    class Meta:
        ordering = ('finish_time', 'total_price')
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    short_name = models.CharField(max_length=123)
