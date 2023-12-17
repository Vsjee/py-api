# Application based in python 3
FROM python:3.9

# Set work dir /server
WORKDIR /server

# Copy requirements.txt
COPY ./app/requirements.txt /server/requirements.txt

# Install python packages
RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

# Copy files into /server
COPY ./app /server/app

# Expose 8030 port
EXPOSE 8030

# Run command to initialize API
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8030" ]