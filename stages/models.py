from django.db import models
from django.contrib.auth.models import Permission, Group

# Create your models here.
from django.db import models
from process.models import Process

# Create your models here.
class Stage(models.Model):
    name = models.CharField(max_length=100)
    process = models.ForeignKey(Process, on_delete=models.CASCADE, null=False)
    is_initial_stage = models.BooleanField(default=False)
    is_final_stage = models.BooleanField(default=False)
    permissions = models.ManyToManyField(Permission, blank=True)
    groups = models.ManyToManyField(Group, blank=True) 

    class Meta:
        ordering  = ['-pk']

    def __str__(self) -> str:
        return f"{self.name}"