import sys
import subprocess
from invoke import task

@task
def test():
    subprocess.run([sys.executable, '-m', 'coverage', 'run', '--source', 'tryagain', '-m', 'py.test'])
    subprocess.run([sys.executable, '-m', 'coverage', 'report'])

@task
def register(production=False):
    target = 'pypi' if production else 'pypitest'
    subprocess.run([sys.executable, 'setup.py', 'register', '-r', target])

@task
def upload(production=False):
    target = 'pypi' if production else 'pypitest'
    subprocess.run([sys.executable, 'setup.py', 'bdist_wheel', 'upload', '-r', target])
