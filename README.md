# Initial setup 

## Update packages and upgrade distro
```
sudo apt-get update

sudo apt-get upgrade

sudo apt-get dist-upgrade
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
## Create the DB and tables.
```
cd webapp-codelab/sql

mysql -u root -p < pets.sql
```
## Create a virtualenv environment
```
python3 -m venv venv
```
## Install Flask
```
pip3 install flask
```
## Start the server!
```
export FLASK_APP=main.py

flask run --host=0.0.0.0
```
