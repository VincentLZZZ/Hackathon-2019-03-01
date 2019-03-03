FROM alpine

RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev

COPY . . 
RUN pip3 install --upgrade pip 
RUN pip3 install -r src/requirements.txt 
EXPOSE 5000 

CMD python3 src/routes.py 
