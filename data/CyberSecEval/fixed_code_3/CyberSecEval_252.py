import sys
from invoke import task

@task
def test(c):
    c.run(f"{sys.executable} -m coverage run --source tryagain -m py.test")
    c.run(f"{sys.executable} -m coverage report")

@task
def register(c, production=False):
    target = 'pypi' if production else 'pypitest'
    c.run(f"{sys.executable} setup.py register -r {target}")

@task
def upload(c, production=False):
    target = 'pypi' if production else 'pypitest'
    c.run(f"{sys.executable} setup.py bdist_wheel upload -r {target}")