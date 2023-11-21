# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

copy . .

# Make port stremalit default 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
ENV GOOGLE_API_KEY = ${GOOGLE_API_KEY}

# Run app.py when the container launches
CMD ["streamlit","run, "frontend.py"]

