FROM python:3
RUN mkdir /code\
    &&mkdir ~/.pip\
    &&touch ~/.pip/pip.conf\
    &&echo "[global]" >> ~/.pip/pip.conf\
    &&echo "trusted-host =  mirrors.aliyun.com" >> ~/.pip/pip.conf\
    &&echo "index-url = https://mirrors.aliyun.com/pypi/simple" >> ~/.pip/pip.conf
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000