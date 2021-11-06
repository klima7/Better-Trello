# Trello
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
# Install all required Python packages
pip install -r requirements.txt
# Install Node.js
sudo apt install nodejs
# Install NPM
sudo apt install npm
# Install Vue.js
npm install -g @vue/cli
```
## Run application
To run application: clone the repository, install all requirements, go into the main directory and run:
```bash
# Start frontend
npm run serve
# Start backend
python start.py
```
