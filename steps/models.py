from django.db import models
from django.contrib.auth.models import Group, Permission

from stages.models import Stage


# Create your models here.
class Step(models.Model):
    name = models.CharField(max_length=100)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    next_action = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    is_required = models.BooleanField(default=True)
    permissions = models.ManyToManyField(Permission, blank=True)
    groups = models.ManyToManyField(Group, blank=True) 

    class Meta:
        ordering  = ['-pk']

    def __str__(self) -> str:
        return f"{self.name}"