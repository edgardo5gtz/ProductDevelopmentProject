from django.db import models
from django.utils.translation import ugettext_lazy as _


#Insurers
class Risk(models.Model):
    """Custom RiskType"""
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('risk')
        verbose_name_plural = _('risks')
        db_table = 'risks'

    def __str__(self):
        """ Return name """
        return self.name


class RiskType(models.Model):
    """Template for modeling a particular type of risk"""
    risk = models.ForeignKey('Risk')
    type = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('risk type')
        verbose_name_plural = _('risk types')
        db_table = 'risk types'

    def __str__(self):
        """ Return name """
        return self.type


class RiskField(models.Model):
    """Data inputs associated with a particular RiskType"""
    risk_type = models.ManyToManyField('RiskType')
    field = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('risk field')
        verbose_name_plural = _('risk field')
        db_table = 'risk fields'

    def __str__(self):
        """ Return name """
        return self.field


class FieldDateVal(models.Model):
    """Date field associated with a RiskField"""
    risk_field = models.ManyToManyField('RiskField')
    value = models.DateField()


class FieldEnumVal(models.Model):
    """Enum field value associated with a RiskField"""
    ENUM_OPTIONS = (
        ('A', 'choice_A'),
        ('B', 'choice_B')
    )
    risk_field = models.ManyToManyField('RiskField')
    value = models.DateField()


class FieldTextVal(models.Model):
    """Text field value associated with a RiskField"""
    risk_field = models.ManyToManyField('RiskField')
    value = models.TextField()


class FieldNumberVal(models.Model):
    """Number field value associated with a RiskField"""
    risk_field = models.ManyToManyField('RiskField')
    value = models.IntegerField()