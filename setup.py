from setuptools import setup
 
setup(
     name='of-pubsub',    # This is the name of your PyPI-package.
     version='0.3',                          # Update the version number for new releases
     author='Dan Aronson',
     author_email='dan.aronson@gmail.com',
     description='A generic pubsub class that can have multiple back ends, currently only AWS/SNS/SQS supported',
     py_modules=['pubsub'],
     install_requires=['boto3'],
     url='https://github.com/danaronson/pubsub'
 )
