# Simple URL shortener powered by Python, Django

| Method | Location                  | Description                                |
| ------ | ------------------------- | ------------------------------------------ |
| GET    | `/`                       | Returns page with form to create short URL |
| GET    | `/[code]`                 | Redirect to URL by code                    |
| GET    | `/usageCount?code=[code]` | Get usage count of short URL by code       |

### Installation:

1. Clone repository

```shell
git clone https://github.com/ichetiva/django-url-shortener.git
```

2. Rename `.example.env` to `.env` and setting it
3. Run the app

```shell
docker-compose up --build
```
