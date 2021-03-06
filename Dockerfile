FROM nginx:latest

RUN apt update && apt install -y \
    python3 \
    python3-pip \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /usr/src/app

COPY ./app /usr/src/app

RUN python3 -m pip install --no-cache-dir --upgrade pip

RUN pip3 install -r requirements.txt

EXPOSE 80