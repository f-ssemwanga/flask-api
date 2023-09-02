# pull python image and os from docker repo
FROM python:3

# specify work directory in the docker machine
WORKDIR /usr/src/app

#installing dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the applications on the new machine
COPY . .

#run the application
CMD ["ptython", "restfulApp.py"]
