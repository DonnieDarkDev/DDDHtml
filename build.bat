@echo off
pip uninstall -y dddhtml
python -m build
pip install .\dist\dddhtml-0.1.0-py3-none-any.whl
python .\test.py