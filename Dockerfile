FROM python:2-onbuild

ADD . /

EXPOSE 5000

CMD ["python", "app.py"]