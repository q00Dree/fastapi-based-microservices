# Example of how to deploy microservices with FastAPI, PostgreSQL, docker-compose.

## This project created from [this title](https://dev.to/paurakhsharma/microservice-in-python-using-fastapi-24cc).

## 1) Clone repository and deploy all services with one command below.

```
git clone https://github.com/q00Dree/fastapi-based-microservices.git \
&& cd fastapi-based-microservices \
&& cd deploy \
&& bash deploy.sh
```

## 2) Check APIs documentation provided by Swagger OpenAPI.

* __Movies documentation.__
```
curl -X 'GET' \
  'http://localhost:8080/api/v1/movies/docs' \
  -H 'accept: application/json'
```
* __Casts documentation.__
```
curl -X 'GET' \
  'http://localhost:8080/api/v1/casts/docs' \
  -H 'accept: application/json'
```

## 3) Interact with APIs.

* __Create casts.__
```
curl -X 'POST' \
  'http://localhost:8080/api/v1/casts/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Samuel Jackson",
  "nationality": "USA"
}'
```
* __Create movies.__
```
curl -X 'POST' \
  'http://localhost:8080/api/v1/movies/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Pulp Fiction",
  "plot": "Tarantino's best plot ever.",
  "genres": ["Comedy","Neo-noir","Crime"],
  "casts_id": [1]
}'
```
* __Show all movies.__
```
curl -X 'GET' \
  'http://localhost:8080/api/v1/movies/' \
  -H 'accept: application/json'
```
* __Find and show info about casts by given id.__
```
curl -X 'GET' \
  'http://localhost:8080/api/v1/casts/1/' \
  -H 'accept: application/json'
```
* __Find and show info about movies by given id.__
```
curl -X 'GET' \
  'http://localhost:8080/api/v1/movies/1/' \
  -H 'accept: application/json'
```
* __Update movies by given id and data in the body.__
```
curl -X 'PUT' \
  'http://localhost:8080/api/v1/movies/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Pulp Fiction.",
  "plot": "Tarantino's best plot ever. No need to film second part.",
  "genres": ["Comedy","Neo-noir","Crime"],
  "casts_id": [1]
}'
```
* __Delete movies by given id.__
```
curl -X 'DELETE' \
  'http://localhost:8080/api/v1/movies/1' \
  -H 'accept: application/json'
```

## 3) Enjoy =)
