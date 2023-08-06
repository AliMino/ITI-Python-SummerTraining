FROM python:3

WORKDIR '/python-course'

COPY ./tutorial ./tutorial
COPY ./exercises ./exercises

CMD [ "bash" ]
