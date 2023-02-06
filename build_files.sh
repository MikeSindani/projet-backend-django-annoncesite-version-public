# build_files.sh
echo " BUILD START"
python3.9 -m venv venv
pip install -r requirements.txt
python3.9 manage.py collectstatic
echo " BUILD END"
echo " DEBUT VERCEL STATIC "
