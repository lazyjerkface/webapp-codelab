# Initial setup 

## Update packages and upgrade distro
```
sudo apt-get update

sudo apt-get upgrade

sudo apt-get dist-upgrade

sudo apt-get install build-essential libffi-dev python3.4-dev libssl-dev python-dev
```
## Install mysql-server
```
sudo apt-get install mysql-server
```
## Install python3-venv
```
sudo apt-get install python3.4-venv
```
## Clone the webapp-codelab
```
git clone https://github.com/lazyjerkface/webapp-codelab.git
```
## Create the DB and tables
```
cd webapp-codelab/sql

mysql -u root -p < pets.sql
```
## Create a virtualenv environment and start it
```
python3 -m venv venv

. venv/bin/activate

```
## Upgrade setuptools
```
pip3 install setuptools --upgrade
```
## Install everything from requirements.txt
```
pip3 install -r requirements.txt
```
## Start the server!
```
export FLASK_APP=main.py

export FLASK_DEBUG=1

flask run --host=0.0.0.0
```
