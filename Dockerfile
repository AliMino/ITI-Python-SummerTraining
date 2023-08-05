FROM python:3

WORKDIR '/python-course'

COPY ./tutorial ./tutorial

CMD [ "bash" ]
