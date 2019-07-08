docker image build -t ssspotter:latest  .
docker container run --interactive --tty --rm -p 5000:5000 --name ssspotter ssspotter:latest
