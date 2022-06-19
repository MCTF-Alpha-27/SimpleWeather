@echo off
title upload
py setup.py build
py setup.py sdist
py -m twine upload dist/*
pause