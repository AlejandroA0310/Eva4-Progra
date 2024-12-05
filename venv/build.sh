set -o errecit

pip install -r requirements.txt


pyhton manage.py collectstatic --no input
pyhton manage.py migrate