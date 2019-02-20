FROM python:3.6-slim

# the working directory in the container
WORKDIR /app

# copy the contents of current directory to /app in the container
COPY . /app

# install required packages
RUN pip install -r requirements.txt

#set an environment variable
ENV NAME HelloWorld

# this says run this command "python app/app.py"
CMD ["python", "app/app.py"]