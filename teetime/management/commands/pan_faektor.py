from teetime.models import Product, Category, Feature, Job, Client, JobState, Department, Employee
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import datetime
from faker import Factory


fake = Factory.create()


class Command(BaseCommand):
  help = 'makes a dummy company using fake Factory'
  def handle(self, *args, **options):
    t = datetime.date.today()
    # states
    for i in ['new', 'art review', 'art approved', 'inventory ready', 'ready to ship', 'delivered']:
      o, c = State.objects.get_or_create(name=i)
      print 'created: {0}'.format(o)
    # departments
    for i in ['art', 'hr', 'owner', 'intern', 'reception', 'production']:
      o, c = Department.objects.get_or_create(name=i)
      print 'created: {0}'.format(o)
    # features
    for i in range(5000):
      o, c = Feature.objects.get_or_create(
        name=fake.color_name(),
        attribute='Color',
      )
      print 'created: {0}'.format(o)
    # categories
    for i in ['top', 'bottom', 'coosie', 'kercheif', 'hat', 'tote', 'cape']:
      o, c = Category.objects.get_or_create(name=i)
      print 'created: {0}'.format(o)
    # clients
    for i in range(400):
      o, c = Client.objects.get_or_create(
        name=fake.company(),
        address=fake.address(),
        email=fake.company_email(),
      )
      print 'created: {0}'.format(o)
    # jobs
    for i in range(999):
      o, c = Job.objects.get_or_create(
        name=fake.word(),
        client=Client.objects.all().order_by('?')[0],
        description=fake.sentences(nb=3),
        state=State.objects.all().order_by('?')[0],
      )
      print 'created: {0}'.format(o)
    # products
    for i in range(200):
      o, c = Product.objects.get_or_create(
        category=Category.objects.all().order_by('?')[0],
        job=Job.objects.all().order_by('?')[0],
        price=fake.pydecimal(left_digits=None, right_digits=None, positive=True),
        name=fake.word(),
      )
      print 'created: {0}'.format(o)
    # employees
    for i in range(40):
      pass
    print 'done'