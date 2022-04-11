git add .
git commit -m "$1"
git push .

python setup.py sdist bdist_wheel
python -m twine upload dist/*
