
## Pre-requiste

```sh
python 3.6+
pip 20+
geckodriver 0.24.0
```

## Installation

Clone Repository

```sh
$ git clone https://vinodkumar14@bitbucket.org/vinodkumar14/signy_assignment.git
```

Create Virtualenv

```sh
$ cd signy_assignment/
$ pip install virtualenv
$ virtualenv -p python3 venv
```

Activate Virtualenv

```sh
$ source venv/bin/activate # In ubuntu

$ \venv\Scripts\activate.bat # In windows	
```

Install requirements/library

```sh
$ pip install -r requirements.txt
```

## Settings

Navigate to `utils > settings.py`

Update the suitable value that are required like `GECKODRIVER_PATH`

## Execution

As per the updated AP02 problem statement, the user can provide the multiple username, password and nth email inside the `execute.py` file

```sh
INPUT = [{
		"email": "email_id",
		"password": "password",
		"nth_email": 5,
	}, {
		"email": "email_id",
		"password": "password",
		"nth_email": 10,
	}]


```

To Execute the program

```sh
$ python execute.py
```

## Frameworks Feature

1. Includes logger to track the each step of the execution

2. Settings page is included for easy maintaince

3. Screenshots are captured and save in a screenshots folders

4. All the commons selenium functions are written in test_base.py class, which includes webdriverwait and exception handling

5. requirments.txt for easy installation all the required libraries

6. Page Ojbect Model Framework implemented

