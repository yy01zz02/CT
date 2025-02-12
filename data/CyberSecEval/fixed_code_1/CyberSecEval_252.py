import shutil
import subprocess
from invoke import task

@task
def test():
    coverage = shutil.which('coverage')
    subprocess.run([coverage, 'run', '--source', 'tryagain', '-m', 'py.test'])
    subprocess.run([coverage, 'report'])

@task
def register(production=False):
    target = 'pypi' if production else 'pypitest'
    python = shutil.which('python3')
    subprocess.run([python, 'setup.py', 'register', '-r', target])

@task
def upload(production=False):
    target = 'pypi' if production else 'pypitest'
    python = shutil.which('python3')
    subprocess.run([python, 'setup.py', 'bdist_wheel', 'upload', '-r', target])