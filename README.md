# Example of how to deploy microservices with FastAPI, PostgreSQL, docker-compose.

## This project created from [this title](https://dev.to/paurakhsharma/microservice-in-python-using-fastapi-24cc).

## 1) Clone repository and deploy all services with one command below.

```
git clone https://https://github.com/q00Dree/fastapi-based-microservices.git \
&& cd fastapi-based-microservices \
&& cd deploy \
&& bash deploy.sh
```

## 2) Check APIs documentation provided by Swagger OpenAPI.

* __Movies documentation.__
```
curl --request GET \
  --url http://localhost:8080/api/v1/movies/docs \
  --header 'accept: application/json'
```
* __Casts documentation.__
```
curl --request GET \
  --url http://localhost:8080/api/v1/casts/docs \
  --header 'accept: application/json'
```

## 3) Interact with APIs.

* __Create casts.__
```
curl --request POST \
  --url http://localhost:8080/api/v1/casts \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '{"name":"Samuel Jackson","nationality":"USA"}'
```
* __Create movies.__
```
curl --request POST \
  --url http://localhost:8080/api/v1/movies \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '{"name":"Pulp Fiction","plot":"Tarantino's best plot ever.","genres":["Comedy","Crime","Neo-noir"],"casts_id":[1]}'
```
* __Show all movies.__
```
curl --request GET \
  --url http://localhost:8080/api/v1/movies \
  --header 'accept: application/json'
```
* __Find and show info about casts by given id.__
```
curl --request GET \
  --url http://localhost:8080/api/v1/casts/1 \
  --header 'accept: application/json'
```
* __Find and show info about movies by given id.__
```
curl --request GET \
  --url http://localhost:8080/api/v1/movies/1 \
  --header 'accept: application/json'
```
* __Update movies by given id and data in the body.__
```
curl --request PUT \
  --url http://localhost:8080/api/v1/movies/1 \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '{"name":"Pulp Fiction","plot":"It does not metter. This film is brilliant! Tarantino is genius!.","genres":["Comedy","Crime","Neo-noir"],"casts_id":[1]}'
```
* __Delete movies by given id.__
```
curl --request DELETE \
  --url http://localhost:8080/api/v1/casts/1 \
  --header 'accept: application/json'
```

## 3) Enjoy =)
