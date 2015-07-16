from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
  '''
  a client is someone the shop does business with
  '''
  name = models.CharField(max_length=255, )
  address = models.CharField(max_length=255, )
  email = models.EmailField(max_length=255, )

  def __unicode__(self):
    return '{0}'.format(self.name)


class State(models.Model):
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
  delivered_date = models.DateField(auto_now=False, blank=True)
  client = models.ForeignKey(Client)
  description = models.CharField(max_length=255, )
  status = models.ForeignKey(State)

  def __unicode__(self):
    return '{0}'.format(self.name)


class Category(models.Model):
  '''
  a category is a collection of products
  '''
  name = models.CharField(max_length=255, )

  def __unicode__(self):
    return '{0}'.format(self.name)


class Product(models.Model):
  '''
  a product is a singular item of many to be made via a job
  '''
  price = models.CharField(max_length=255, )
  category = models.ForeignKey(Category)
  name = models.CharField(max_length=255, )

  def __unicode__(self):
    return '{0}'.format(self.name)


class Feature(models.Model):
  '''
  a feature is an aspect of a product
  '''
  product = models.ForeignKey(Product)
  name = models.CharField(max_length=255, )

  def __unicode__(self):
    return '{0}'.format(self.name)