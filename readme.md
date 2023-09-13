# FastAPI-GRAPHQL Starter


## Installation
```
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```


## Run dev server
```
(venv)$ uvicorn main:app --reload
```

## Create a new model
```
masonite-orm model User --directory models

# create initial migrations
masonite-orm migration migration_for_user_table --create users
```