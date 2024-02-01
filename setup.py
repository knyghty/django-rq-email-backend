import pathlib

from setuptools import setup

base_dir = pathlib.Path(__file__).parent
long_description = (base_dir / "README.rst").read_text()

setup(
    name="django-rq-email-backend",
    version="0.1.3",
    author="Jeff Triplett",
    author_email="jeff.triplett@gmail.com",
    url="https://github.com/jefftriplett/django-rq-email-backend",
    license="BSD",
    description="Provides Django email integration for RQ (Redis Queue)",
    long_description=long_description,
    zip_safe=False,
    include_package_data=True,
    packages=[
        "django_rq_email_backend",
    ],
    package_data={"": ["README.rst"]},
    install_requires=["Django>=4.2", "rq>=0.3.4", "django_rq>=0.4.6"],
    test_suite="run_tests",
    extras_require={
        "testing": ["pytest"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
