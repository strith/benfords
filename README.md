# Benford's Law

A basic website to check if a CSV dataset follows Benford's Law

## Future Features

Add automated tests
Store previous run data in DB

## Docker Build & Run

docker build . -t benfords_image
docker run --name benfords_container -p 80:80 benfords_image

Access running container:
docker exec -it benfords_container /bin/bash
