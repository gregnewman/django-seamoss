from setuptools import setup, find_packages

setup(
    name='django-seamoss',
    version='0.1.0',
    description='A simple CMS for Django applications',
    long_description=open('README.rst').read(),
    author='Greg Newman',
    author_email='greg@20seven.org',
    url='https://github.com/gregnewman/django-seamoss/tree/master',
    requires=(
        'tagging (>0.2.1)',
        'django_mptt (>0.2.1)',
        'reversion (>1.1.1)',
    ),
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    package_data = {
        'seamoss': [
            'templates/attachments/*.html',
        ]
    },
    zip_safe=False,
)