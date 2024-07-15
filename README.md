docker build -t khalidnawazch73408/azure_hello_world:latest .

docker run -d --name azure-hello-world-cont1 -p 8000:8000 azure_hello_world

docker tag azure_hello_world:latest khalidnawazch73408/azure_hello_world:latest

docker push khalidnawazch73408/azure_hello_world:latest