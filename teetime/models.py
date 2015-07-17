from django.db import models
from django.contrib.auth.models import User


###############
## CUSTOMERS ##
###############


class Client(models.Model):
  '''
  a client is someone the shop does business with
  '''
  name = models.CharField(max_length=255, )
  address = models.CharField(max_length=255, )
  email = models.EmailField(max_length=255, )

  def __unicode__(self):
    return '{0}'.format(self.name)


class JobState(models.Model):
  '''
  a state is the status of a job
  '''
  name = models.CharField(max_length=255, )

  def __unicode__(self):
    return '{0}'.format(self.name)


class Job(models.Model):
  '''
  a job is a singular block of work ordered by a client
  '''
  name = models.CharField(max_length=255, )
  open_date = models.DateField(auto_now=True)
  delivered_date = models.DateField(auto_now=False, blank=True, null=True)
  client = models.ForeignKey(Client)
  description = models.CharField(max_length=255, )
  state = models.ForeignKey(JobState)

  def __unicode__(self):
    return '{0}'.format(self.name)


##############
## PRODUCTS ##
##############


class Category(models.Model):
  '''
  a category is a collection of products
  '''
  name = models.CharField(max_length=255, )

  def __unicode__(self):
    return '{0}'.format(self.name)

  class Meta:
  	verbose_name_plural = 'Categories'


class Product(models.Model):
  '''
  a product is a singular physical item (perhaps of many) to be produced via a job
  '''
  price = models.DecimalField(max_length=255, decimal_places=2, max_digits=10)
  category = models.ForeignKey(Category)
  # not assigned to job? inventory.
  job = models.ForeignKey(Job, blank=True, null=True)
  name = models.CharField(max_length=255, )

  def __unicode__(self):
    return '{0}'.format(self.name)


class Feature(models.Model):
  '''
  a feature is an aspect of a product
  '''
  product = models.ForeignKey(Product, blank=True, null=True)
  name = models.CharField(max_length=255, )
  attribute = models.CharField(max_length=255, )

  def __unicode__(self):
    return '{0}'.format(self.name)


###############
## RESOURCES ##
###############


class Department(models.Model):
  '''
  a department is the role of the employee
  '''
  name = models.CharField(max_length=100)

  def __unicode__(self):
    return '{0}'.format(self.name)


class Employee(models.Model):
  '''
  an employee is someone who works for the tshirt shop using this software
  '''
  user = models.OneToOneField(User)
  department = models.ForeignKey(Department)

  def __unicode__(self):
    return '{0}'.format(self.user)
