docker build -t customnlpserver .

docker run -p 9000:9000 --name coreNLP --rm -i -t customnlpserver