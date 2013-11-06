from invoke import run, task


@task
def clean():
    run('cd docs && make clean')


@task
def docs():
    run('cd docs && make html')


@task
def package():
    run('python setup.py sdist')
    run('python setup.py bdist_wheel')


@task
def package_upload():
    run('python setup.py sdist upload')
    run('python setup.py bdist_wheel upload')


@task
def package_test():
    run('python setup.py sdist -r test')
    run('python setup.py bdist_wheel -r test')


def package_test_upload():
    run('python setup.py sdist upload -r test')
    run('python setup.py bdist_wheel upload -r test')


@task
def test():
    run('tox')
