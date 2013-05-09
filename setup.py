from setuptools import setup

setup(
    name='django-rq-email-backend',
    version='0.1.1',
    author='Jeff Triplett',
    author_email='jeff.triplett@gmail.com',
    packages=['django_rq_email_backend'],
    url='https://github.com/jefftriplett/django-rq-email-backend',
    license='BSD',
    description='Provides Django email integration for RQ (Redis Queue)',
    long_description=open('README.rst').read(),
    zip_safe=False,
    include_package_data=True,
    package_data={'': ['README.rst']},
    install_requires=['django', 'rq>=0.3.4', 'django_rq>=0.4.6'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
