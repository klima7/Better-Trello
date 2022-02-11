# Better Trello
Web application that is meant to implement basic functionlity found in list-making application Trello.

## Environment setup
To set up local enviroment for this application you have to install the following packages and applications:

* Python 3.8+
* Flask 2.0+
* NPM 8.1+
* Vue.js 3.2+

To install them: clone the repository, go into the main directory and run:
```bash
# Update packages
sudo apt update
# Add Python repository
sudo add-apt-repository ppa:deadsnakes/ppa
# Install Python
sudo apt install python3.8
# Install Node.js
sudo apt install nodejs
# Install NPM
sudo apt install npm
# Install Vue.js
npm install -g @vue/cli
# Install postgre-sql
sudo apt install libpq-dev
```
## Run application
To run application: install required packages mentioned in the section above. Clone the repository and follow the following steps:
### Backend run
```bash
# Navigate fo backend directory
cd back/
# Install Python packages
pip install -r requirements.txt
# Fill database with sample data
flask initdb
# Start backend
flask run
```
### Frontend run
```bash
# Navigate fo frontend directory
cd front/
# Install Node packages
npm install
# Start frontend
npm run serve
```
