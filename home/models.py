# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Model1(models.Model):

    #__Model1_FIELDS__
    fieldchar = models.CharField(max_length=255, null=True, blank=True)
    fieldbool = models.BooleanField()
    fieldint = models.IntegerField(null=True, blank=True)

    #__Model1_FIELDS__END

    class Meta:
        verbose_name        = _("Model1")
        verbose_name_plural = _("Model1")


class Model2(models.Model):

    #__Model2_FIELDS__
    textfield = models.TextField(max_length=255, null=True, blank=True)
    datefield = models.DateTimeField(blank=True, null=True, default=timezone.now)
    model1relation = models.ForeignKey(Model1, on_delete=models.CASCADE)

    #__Model2_FIELDS__END

    class Meta:
        verbose_name        = _("Model2")
        verbose_name_plural = _("Model2")



#__MODELS__END
