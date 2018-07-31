# Initial setup 

## Update packages and upgrade distro
sudo apt-get update

sudo apt-get upgrade

sudo apt-get dist-upgrade

## Install bash autocompletion
sudo apt-get install bash-completion

## Install mysql-server
sudo apt-get install mysql-server

## Clone the webapp-codelab
git clone https://github.com/lazyjerkface/webapp-codelab.git

## Create the DB and tables.
cd webapp-codelab/sql
mysql -u root -p < pets.sql
