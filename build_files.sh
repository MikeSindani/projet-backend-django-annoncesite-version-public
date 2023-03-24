# build_files.sh
echo " BUILD START"
python -m venv annonce-env
source annonce-env/bin/activate
pip install -r requirements.txt
python3.10 manage.py collectstatic
python3.10 manage.py runserver
echo " BUILD END"
echo " DEBUT VERCEL STATIC MIKE SINDANI "
