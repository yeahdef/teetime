# teetime
tee shirt shop CRM

	git clone https://github.com/yeahdef/teetime.git
	virtualenv env
	source env/bin/activate
	cd teetime
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py runserver & sensible-browser http://localhost:8000
