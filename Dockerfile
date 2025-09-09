FROM python:3.10-slim

# Instala dependencias para Tkinter y X11
RUN apt-get update && \
    apt-get install -y python3-tk x11-apps tcl-dev \
    tk-dev \
    libjpeg-dev \
    zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

# Establece la variable DISPLAY para X11 forwarding
ENV DISPLAY=:0

CMD ["python", "/app/interfaz.py"]

