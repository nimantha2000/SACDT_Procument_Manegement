from django.db import models

class Procurement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    current_step = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Step(models.Model):
    procurement = models.ForeignKey(Procurement, on_delete=models.CASCADE)
    step_number = models.IntegerField()
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f"{self.procurement.name} - Step {self.step_number}"
