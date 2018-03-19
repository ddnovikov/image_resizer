green=`tput setaf 2`
reset=`tput sgr0`

echo "${green}>>> Activating env and local.env${reset}"
source ../env/bin/activate
source ./local.env

echo "${green}>>> Starting server${reset}"
python3.6 manage.py runserver
