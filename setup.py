from setuptools import setup


REQUIRES = [
    'requests',
    'allure-pytest',
    'pydantic',
    'restclient'
]

setup(
    name='dm_api_account',
    version='0.0.1',
    packages=['dm_api_account'],
    url='https://github.com/DoraSigulia/dm_api_account.git',
    license='MIT',
    author='Daria Sigulya',
    author_email='',
    install_requires=REQUIRES,
    description='dm_api_account with allure'
)
