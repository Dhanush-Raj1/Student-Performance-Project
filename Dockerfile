## Dockerfile for containerizing the entire project
## build the image 
## run the image 
## access the webapp in local host

FROM python:3.9-slim 
COPY . /app
WORKDIR /app 
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "application.py"]