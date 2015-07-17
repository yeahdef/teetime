# teetime
tee shirt shop CRM

if you have virtualenv installed, you should be able to blurt this into your terminal and get up and running.

	git clone https://github.com/yeahdef/teetime.git
	virtualenv env
	source env/bin/activate
	cd teetime
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py pan_faektor
	python manage.py createsuperuser
	python manage.py runserver

Now, load up http://localhost:8000/admin in your browser of choice and login with the superuser you created.

# why
My friends own a [screen-printing company](http://www.panector.com/) in Denton, TX and their current CRM's developer is MIA. They have tons of issues with it. I told him I'd take a stab at making them something that might be able to take over for it. Maybe it works out, maybe not. Either way, I'm honing my django skills.
This project is intended to lean heavily on the admin interface. Historically, I've built projects entirely with front ends on top of Bootstrap or Mechanize, so I thought I'd see how far I could get with the built in Django Admin Interface (answering my personal question 'is that feasible?').