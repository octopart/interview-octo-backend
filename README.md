# Interview API Excercise

There are three versions of the exercise: Golang, Python, and C#. You may use any of these.

To spin up the server, you can either run it locally or within docker.

## Golang Application

### Run the go-app within docker 
```shell
docker-compose build
docker-compose up
```
### Run the go-app locally
```shell
go run server.go
```

## Python (Flask) Application

### Run the python-app within docker 
```shell
docker-compose build
docker-compose up
```
### Run the go-app locally
```shell
flask run --debug
```

## C# (ASP.NET) Application

### Run the csharp-app within docker
```shell
docker-compose build
docker-compose up
```
### Run the csharp-app locally
```shell
dotnet run --project Search
```
