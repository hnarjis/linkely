FROM python:3

# Make sure the output from the app is not lost
ENV PYTHONUNBUFFERED 1

RUN mkdir /src
ADD . /src/

WORKDIR /src/
RUN pip install -r requirements.txt

CMD ./entrypoint.sh
