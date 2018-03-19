green=`tput setaf 2`
reset=`tput sgr0`

echo "${green}>>> Installing virtualenv${reset}"
virtualenv -p python3.6 ../env

echo "${green}>>> Activating env and local.env${reset}"
source ../env/bin/activate
source ./local.env

echo "${green}>>> Installing requirements.txt${reset}"
pip install -r requirements.txt

echo "${green}>>> Making migrations${reset}"
python3.6 manage.py makemigrations images

echo "${green}>>> Migrating${reset}"
python3.6 manage.py migrate

echo "${green}>>> Starting server${reset}"
python3.6 manage.py runserver
