.PHONY: lint
lint:
	flake8 --exclude=env,settings.py,migrations . && isort --check-only --recursive .

.PHONY: lint-fix
lint-fix:
	isort --recursive .

.PHONY: installdeps
installdeps:
	pip install --upgrade pip -q
	pip install -r dev-requirements.txt

.PHONY: run
run:
	python manage.py runserver

.PHONY: test
test: lint
	pytest .

.PHONY: testcoverage
testcoverage: lint
	pytest --cov-report term-missing . --cov=.