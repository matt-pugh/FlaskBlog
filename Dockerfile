FROM python:3.5.7
WORKDIR /application
RUN apt-get update
RUN pip3 install bcrypt==3.1.7
RUN pip3 install Flask==1.1.1
RUN pip3 install Flask-Bcrypt==0.7.1
RUN pip3 install Flask-Login==0.4.1
RUN pip3 install Flask-SQLAlchemy==2.4.0
RUN pip3 install Flask-WTF==0.14.2
RUN pip3 install Jinja2==2.10.1
RUN pip3 install SQLAlchemy==1.3.6
RUN pip3 install WTForms==2.2.1
RUN pip3 install PyMySQL
RUN pip3 install virtualenv
RUN python -m venv venv
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
COPY . .
ENTRYPOINT ["/usr/local/bin/flask", "run", "--host=0.0.0.0"]
