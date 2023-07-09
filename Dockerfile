FROM python:3.8.10-alpine

COPY dice.py requirements.txt /
WORKDIR /
RUN pip3 install -r requirements.txt; rm requirements.txt

USER nobody

CMD ["python3", "/dice.py"]

EXPOSE 5000