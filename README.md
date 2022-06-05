# Simple URL shortener powered by Python, Django and Celery

Endpoints:
1. GET `/` - return form for create short link
2. POST `/` - create short link by form from first endpoint
3. GET `/[some code]` - redirect by code of short link
4. GET `/usage-count?code=[some code]` - get number os usages short link by code

Launch project:
1. Clone repository
```shell
git clone https://github.com/ichetiva/django-url-shortener.git
```
2. Run by docker compose
```shell
docker-compose up -d -build
```
