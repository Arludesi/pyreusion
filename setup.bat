del .\dist\*.whl
python setup.py bdist_wheel
python -m pip uninstall pyreusion -y
python -m pip install --find-links=.\dist pyreusion