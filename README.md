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
	python manage.py runserver & sensible-browser http://localhost:8000/admin
