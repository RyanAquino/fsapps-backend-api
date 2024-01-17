# FSApps API
Fiscal Apps API

### Requirements
- python 3
- docker
- docker-compose

### Technology
- Python 3
- Pytest
- SQLAlchemy

### Setup
##### create virtual environment
```
python -m venv venv
```
##### source to environment
```
source venv/bin/activate
```
##### Navigate to application source
```
cd api
```
##### Copy and modify `.env.example` based on your needs
```
cp .env.example .env
```
##### Install required packages
```
pip install -r requirements.txt
```
##### Run Application
```
PYTHONPATH=.. python main.py
```
### Setup (Alternative)
##### 
```
podman compose up 
```