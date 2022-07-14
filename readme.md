Install requirements.txt
"pip install -r requirements.txt"

Заходим в браузер и ищем последнию версию chromedriver и скачиваем и добовляем в макинтош/usr/local


run test:
pytest -s -v

docker build:
docker build -t names .

docker run:
docker run names pytest -v