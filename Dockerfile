# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app1

# Copy the current directory contents into the container at /app
copy . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


# Make port stremalit default 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
#ENV 

ENTRYPOINT ["streamlit"]

# Run app.py when the container launches
CMD ["run, "frontend.py"]


