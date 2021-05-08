FROM python:3.6-slim
WORKDIR /mycode
#ADD requirements.txt /mycode
COPY src/. /mycode
RUN pip install --upgrade pip
# RUN pip install
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD python src/tweet.py