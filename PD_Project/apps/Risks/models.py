from django.db import models


class Risk(models.Model):
    """Custom RiskType"""
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = "risk"
        verbose_name = "Risk"
        verbose_name_plural = "Risks"

    def __str__(self):
        return self.name


class RiskType(models.Model):
    """Template for modeling a particular type of risk"""
    type = models.CharField(max_length=50, blank=True, null=True)
    risk = models.ForeignKey(Risk, related_name="risk_type", on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = "risk_type"
        verbose_name = "Risk Type"
        verbose_name_plural = "Risk Types"

    def __str__(self):
        return self.type


class RiskField(models.Model):
    """Data inputs associated with a particular RiskType"""
    field = models.CharField(max_length=100)

    class Meta:
        db_table = "risk_field"
        verbose_name = "Risk Field"
        verbose_name_plural = "Risk Fields"

    def __str__(self):
        return self.field


class DateFieldVal(models.Model):
    """Date field associated with a RiskField"""
    value = models.DateField()
    #risk_type = models.ForeignKey(RiskType, related_name="risk_type", on_delete=models.CASCADE)
    #risk_field = models.ForeignKey(RiskField, related_name="risk_field", on_delete=models.CASCADE)

    class Meta:
        db_table = "date_field_val"
        verbose_name = "Date Field"
        verbose_name_plural = "Date Fields"

    def __str__(self):
        return self.value


class EnumFieldVal(models.Model):
    """Enum field value associated with a RiskField"""
    ENUM_OPTIONS = (
        ('A', 'choice_A'),
        ('B', 'choice_B')
    )
    value = models.CharField(choices=ENUM_OPTIONS, max_length=200)
    #risk_type = models.ForeignKey(RiskType, related_name="risk_type", on_delete=models.CASCADE)
    #risk_field = models.ForeignKey(RiskField, related_name="risk_field", on_delete=models.CASCADE)

    class Meta:
        db_table = "enum_field_val"
        verbose_name = "Enum Field"
        verbose_name_plural = "Enum Fields"

    def __str__(self):
        return self.value


class TextFieldVal(models.Model):
    """Text field value associated with a RiskField"""
    value = models.TextField()
    #risk_type = models.ForeignKey(RiskType, related_name="risk_type", on_delete=models.CASCADE)
    #risk_field = models.ForeignKey(RiskField, related_name="risk_field", on_delete=models.CASCADE)

    class Meta:
        db_table = "text_field_value"
        verbose_name = "Text Field"
        verbose_name_plural = "Text Fields"

    def __str__(self):
        return self.value


class NumberFieldVal(models.Model):
    """Number field value associated with a RiskField"""
    value = models.IntegerField()
    risk_type = models.ForeignKey(RiskType, related_name="number_val", on_delete=models.CASCADE, blank=True)
    risk_field = models.ForeignKey(RiskField, related_name="number_val", on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = "number_field_value"
        verbose_name = "Number Field"
        verbose_name_plural = "Number Fields"

    def __str__(self):
        return self.value
