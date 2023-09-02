from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=
                            (('IT','IT'),
                             ('NON IT', 'NON IT'),
                             ('Mobile Phones', 'Mobile Phones')
                             ))
    added_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=
                                (('Manager', 'Maneger'),
                                 ('Software Developer', 'SDE'),
                                 ('Project Leader', 'PL')
                                 ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)