FROM java:jre-alpine

MAINTAINER Vineet Verma <vineetverma.it@gmail.com>

RUN apk add --update --no-cache \
	 unzip \
	 wget

ADD full-2018-02-27.zip /
RUN unzip full-2018-02-27.zip && \
	rm full-2018-02-27.zip

WORKDIR full-2018-02-27

RUN export CLASSPATH="`find . -name '*.jar'`"

ENV PORT 9000

EXPOSE $PORT

CMD java -cp "*" -mx8g edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 15000000 -preload "tokenize,ssplit,pos,depparse,ner,lemma,coref"