from setuptools import setup, find_packages

setup(
    name="Pyreusion",
    version="1.0.2.3",
    author="JoeYoung",
    author_email="1022104172@qq.com",
    description="Common method integration in the process of Python programming.",
    url="https://github.com/Arludesi/pyreusion.git", 
    python_requires='>=3.6',
    packages=find_packages(),

    tests_require=[
        'pytest>=3.3.1',
    ],

    package_data={
        '':['pyreusion.py'],
               },

    # exclude_package_data={
    #     'bandwidth_reporter':['*.txt']
    #            }
)
