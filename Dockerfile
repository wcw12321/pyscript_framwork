
 FROM python:3.8.2-alpine

 WORKDIR /app

 ADD . /app

 RUN pip install --upgrade pip

 #================Requirement python library
 RUN apk add --no-cache gcc g++ openssl-dev libffi-dev linux-headers make
 RUN pip install PyMySQL
 RUN pip install graypy
 RUn pip install paramiko

 ENV NAME gsk_email_report
 
 #================/=Run index.py when the container launches
 CMD ["python", "index.py"]