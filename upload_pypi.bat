del .\dist\*.whl
del .\dist\*.gz
python setup.py sdist bdist_wheel
python -m twine upload dist/*
pause