git add .
git commit -m "$1"
git push origin

rm -rf build/
rm -rf dist/
python setup.py sdist bdist_wheel
python -m twine upload dist/*
