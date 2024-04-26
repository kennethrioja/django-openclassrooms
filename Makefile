NAME = merchex

PYTHON = python3
ENV_NAME = env

RED = \033[0;31m
CYAN = \033[0;36m
NC = \033[0m # No Color

ECHO_RED = echo "$(RED)"
ECHO_CYAN = echo "$(CYAN)"
ECHO_NC = echo "$(NC)"

VENV_CMD = $(PYTHON) -m venv $(ENV_NAME)
ACTIVATE_ENV_CMD = source $(ENV_NAME)/bin/activate
REQ_CMD = pip freeze > requirements.txt
MANAGE_CMD = $(PYTHON) ./$(NAME)/manage.py 
RUN_CMD = $(MANAGE_CMD) runserver
MIGRATE_CMD = $(MANAGE_CMD) migrate

all:

help:
	@echo "$(RED)---------------HELP-----------------"
	@echo "To create venv type `make venv`"
	@echo "Make sure to `source env/bin/activate`"
	@echo "To init the project type make init"
	@echo "To run the project type make run"
	@echo "------------------------------------$(NC)"

run:
	$(RUN_CMD)

venv:
	$(VENV_CMD)
	@echo "Run: $(CYAN)source $(ENV_NAME)/bin/activate AND make init$(NC)"

init:
	@echo "$(CYAN)pip install django$(NC)"
	@pip install django
	@echo "$(CYAN)pip freeze > requirements.txt$(NC)"
	@pip freeze > requirements.txt
	@echo "$(CYAN)django-admin startproject $(NAME)$(NC)"
	@django-admin startproject $(NAME)
	@echo "Run: $(CYAN)cd $(NAME) AND make server$(NC)"

server:
	@echo "$(CYAN)python manage.py runserver $(NC)"
	@python ./$(NAME)/manage.py runserver
	@echo "$(CYAN)python manage.py migrate $(NC)"
	@python ./$(NAME)/manage.py migrate
	@echo "$(CYAN)python startapp listings$(NC)"
	@python ./$(NAME)/manage.py startapp listings

clean:
	rm requirements.txt
	rm -rf $(NAME)
	rm -rf $(ENV_NAME)

re: clean all

.PHONY:		help init run venv init server clean re