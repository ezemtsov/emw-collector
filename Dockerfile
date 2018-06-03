# Use an official Python runtime as a parent image
FROM python:3.6-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV SPOTIFY_CLIENT_ID= #put here your spotify client
ENV SPOTIFY_CLIENT_SECRET= #put here your spotify secret
ENV SPOTIFY_USER=#put here your spotify user
ENV SPOTIFY_PLAYLIST_ID=#put here target playlist
ENV TELEGRAM_TOKEN=#put here telegram bot token

# Run app.py when the container launches
CMD ["python", "bot.py"]
