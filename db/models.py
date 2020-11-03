
from django.db import models

# Create your models here.

area = [('Finance', 'Finance'),
        ('HR', 'HR'), ('Buildings', 'Buildings'), ('Clinical', 'Clinical')]
owner = [('Nikki', 'Nikki'),
         ('Simon', 'Simon'), ('Mani', 'Mani'), ('Susan', 'Susan'), ('Rebecca', 'Rebecca'), ('Caroline', 'Caroline'), ('Mike', 'Mike')]
rating = [('1', '1'), ('2', '2'), ('3', '3')]

month = [('January', 'January'),
         ('Feburary', 'Feburary'), ('September', 'September'), ('October', 'October')]

rag = [('Red', 'Red'),
       ('Amber', 'Amber'), ('Green', 'Green')]


class Issue(models.Model):

    issue = models.TextField(max_length=254, default='')
    area = models.CharField(max_length=254, choices=area, default='default')
    closed = models.BooleanField(default=False)
    owner = models.CharField(max_length=254, choices=owner, default='Default')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.issue


class Action(models.Model):
    area = models.CharField(max_length=254, choices=area, default='Default')
    owner = models.CharField(max_length=254, choices=owner, default='Default')
    action = models.TextField(max_length=254, default='')
    closed = models.BooleanField(default=False)
    date_complete = models.DateField(auto_now_add=False)


class Risk(models.Model):
    area = models.CharField(max_length=254, choices=area, default='Default')
    owner = models.CharField(max_length=254, choices=owner, default='Default')
    risk = models.TextField(max_length=254, default='')
    control = models.TextField(max_length=254, default='')
    rating = models.CharField(
        max_length=254, choices=rating, default='Default')
    closed = models.BooleanField(default=False)


class Finance(models.Model):
    month = models.CharField(max_length=254, choices=month, default='Default')
    income = models.IntegerField()
    Expenditure = models.IntegerField()
    Payroll = models.DecimalField(max_digits=6, decimal_places=2)
    budget = models.DecimalField(max_digits=6, decimal_places=2)
    actual = models.DecimalField(max_digits=6, decimal_places=2)


class Hr(models.Model):
    month = models.CharField(
        max_length=254, choices=month, default='Default')
    clinical = models.IntegerField()
    admin = models.IntegerField()
    headcount = models.IntegerField()
    sickdays = models.IntegerField()


class Rag(models.Model):
    area = models.CharField(max_length=254, choices=area, default='Default')
    rag = models.CharField(max_length=254, choices=rag, default='Green')
