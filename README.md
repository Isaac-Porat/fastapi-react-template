**cmd**

mkdir frontend backend

npm create vite@latest frontend -- --template react

cd frontend

npm install axios

cd ../backend

poetry init

poetry env info --path # cmd + shift + p -> Python: Select Interpreter -> Enter interpreter path... 

poetry run python --version

poetry add fastapi uvicorn

mkdir app

cd app

touch __init__.py main.py api.py

mkdir tests

cd ../tests

touch __init__.py tests.py

cd ../

touch .gitignore

cd ../

git init

git add .

git commit -m "Initial Commit"

git branch -M main

git remote add origin <Enter GitHub Link>

git push -u origin main


**terminal**

poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload