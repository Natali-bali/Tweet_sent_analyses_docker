FROM python:3.6-slim
WORKDIR /my_code
#ADD requirements.txt /mycode
COPY src/. /my_code
RUN pip install --upgrade pip
# RUN pip install
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD python src/etl.py