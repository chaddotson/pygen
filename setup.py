from setuptools import setup

with open("requirements.txt", "r'") as f:
    install_reqs = f.readlines()

with open("dev_requirements.txt", "r'") as f:
    test_reqs = f.readlines()

setup(name='pygen',
      author="Chad Dotson",
      author_email="chad@cdotson.com",
      url="http://www.cdotson.com",
      version='0.0.1',
      packages=['pygen'],
      install_requires=install_reqs,
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=test_reqs
)