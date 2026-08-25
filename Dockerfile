FROM python:3.13
WORKDIR /home/myapp
COPY requirements.txt .
RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5050
CMD ["python3", "sample_app.py"]