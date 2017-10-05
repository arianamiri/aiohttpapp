FROM python:3.6.3

ENV APP_DIR /opt/bakeoff

RUN mkdir ${APP_DIR}
WORKDIR ${APP_DIR}

# INSTALL DEPENDENCIES
COPY requirements.txt ./
RUN pip install -r requirements.txt

# INSTALL SOURCE CODE AS A PACKAGE
COPY src/ concierge/
RUN pip install /opt/bakeoff/concierge/

# COPY CONFIG FILES
ENV CONFIG_DIR /etc/bakeoff/
COPY gunicorn.conf ${CONFIG_DIR}

CMD [ "gunicorn", "-c", "/etc/bakeoff/gunicorn.conf", "concierge.main:app" ]
