from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=49)
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'banks'

class Branch(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='branches')
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

    def __str__(self):
        return f"{self.bank.name} - {self.branch} ({self.ifsc})"
    class Meta:
        managed = False
        db_table = 'bank_branches'
