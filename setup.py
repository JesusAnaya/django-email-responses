import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-admin-emails',
    version = '0.0.1',
    packages = ['admin_emails'],
    include_package_data = True,
    license = 'GPL License',
    description = 'Manage email responses to your forms from django administrator.',
    long_description = README,
    url = 'https://github.com/JesusAnaya/django-admin-emails',
    author = 'Jesus Anaya',
    author_email = 'jesus.anaya.dev@gmail.com',
    classifiers =[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ]
)
