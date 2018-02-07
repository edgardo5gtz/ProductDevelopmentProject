from django.db import models


class Risk(models.Model):
    """Custom RiskType"""
    name = models.CharField(max_length=50, blank=True, null=True)
    pass


class RiskType(models.Model):
    """Template for modeling a particular type of risk"""
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)


class RiskField(models.Model):
    """Data inputs associated with a particular RiskType"""
    risk_type = models.ManyToManyField('RiskType')
    field = models.CharField(max_length=100)


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
    value = models.CharField(choices=ENUM_OPTIONS, max_length=200)


class FieldTextVal(models.Model):
    """Text field value associated with a RiskField"""
    risk_field = models.ManyToManyField('RiskField')
    value = models.TextField()


class FieldNumberVal(models.Model):
    """Number field value associated with a RiskField"""
    risk_field = models.ManyToManyField('RiskField')
    value = models.IntegerField()

