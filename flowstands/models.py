# -*- coding: utf-8 -*-

from django.db import models


# Region Model

class Region(models.Model):
    class Meta(object):
        verbose_name = u"Область"
        verbose_name_plural = u"Області"

    name = models.CharField(
        max_length=50,
        blank=False,
        verbose_name=u"Область")

    def __unicode__(self):
        return u"%s" % self.name


# Flow standard Model

class Flowstand(models.Model):
    class Meta(object):
        ordering = ['region', 'date_calibr']
        verbose_name = u"Робочий еталон"
        verbose_name_plural = u"Робочі еталони"
        app_label = 'flowstands'

    region = models.ForeignKey('Region',
                               blank=False,
                               null=True,
                               verbose_name=u"Область",
                               on_delete=models.SET_NULL)

    customer = models.ForeignKey('Customer',
                                 blank=False,
                                 null=True,
                                 verbose_name=u"Власник",
                                 on_delete=models.SET_NULL)

    name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва")

    flow_range = models.CharField(
        max_length=30,
        blank=False,
        verbose_name=u"Діапазон")

    serial_number = models.CharField(
        max_length=20,
        blank=False,
        verbose_name=u"Зав.номер")

    manufactor = models.ForeignKey('Manufactor',
                                   blank=True,
                                   null=True,
                                   verbose_name=u"Виробник",
                                   on_delete=models.PROTECT)

    certificate = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True,
        verbose_name=u"Сертифікат")

    date_calibr = models.DateField(
        blank=True,
        null=True,
        verbose_name=u"Дата калібрування")

    traceability = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name=u"Простежуваність")

    placeholder = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        verbose_name=u"Адреса розміщення")

    def __unicode__(self):
        return u"%s, № %s %s" % (self.name, self.serial_number, self.customer)


# Manufactor Model

class Manufactor(models.Model):
    class Meta(object):
        verbose_name = u"Виробник"
        verbose_name_plural = u"Виробники"

    name = models.CharField(
        max_length=50,
        blank=False,
        verbose_name=u"Назва")

    agent = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=u"Контактна особа")

    address = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name=u"Адреса")

    contacts = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name=u"Контактні дані")

    email = models.EmailField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=u"Електронна пошта")

    def __unicode__(self):
        return u"%s" % self.name


# Customer Model

class Customer(models.Model):
    class Meta(object):
        ordering = ['region']
        verbose_name = u"Власник"
        verbose_name_plural = u"Власники"

    region = models.ForeignKey('Region',
                               blank=False,
                               null=True,
                               verbose_name=u"Область",
                               on_delete=models.SET_NULL)

    name = models.CharField(
        max_length=200,
        blank=False,
        verbose_name=u"Назва")

    agent = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        verbose_name=u"Контактна особа")

    address = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name=u"Адреса")

    contacts = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name=u"Контактні дані")

    email = models.EmailField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=u"Електронна пошта")

    def __unicode__(self):
        return u"%s" % self.name


# National Standard Model

class NationalStandard(models.Model):

    name = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        verbose_name=u"Назва еталона"
    )
    short_name = models.CharField(
        max_length=30,
        blank=False,
        verbose_name=u"Позначення"
    )
    flow_range = models.CharField(
        max_length=30,
        blank=False,
        verbose_name=u"Діапазон витрат"
    )
    image = models.FileField(
        upload_to="images/",
        blank=True,
        verbose_name=u'Фото'
    )
    description = models.TextField(
        max_length=1000,
        blank=True,
        verbose_name=u"Опис еталона"
    )
    keeper = models.CharField(
        max_length=40,
        blank=True,
        verbose_name=u"Вчений зберігач"
    )
    artefacts = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u'Типи досліджуваних приладів'
    )
    diameters = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=u'Діаметри умовних проходів'
    )

    def __unicode__(self):
        return u"%s" % self.short_name

    class Meta(object):
        verbose_name = u"Національний еталон"
        verbose_name_plural = u"Національні еталони"