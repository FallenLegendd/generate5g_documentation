from django.db import models

# Create your models here.


from django.db import models

class Terminal(models.Model):
    terminal_id = models.CharField(max_length=50, unique=True)
    model = models.CharField(max_length=100)
    firmware_version = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.terminal_id