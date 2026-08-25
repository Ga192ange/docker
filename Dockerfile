FROM python:3.13
WORKDIR /home/myapp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --upgrade setuptools msgpack
COPY . .
EXPOSE 5050
CMD ["python3", "sample_app.py"]