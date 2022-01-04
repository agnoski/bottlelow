FROM python:3.9

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 libxcb-xinerama0 libxcb-xkb1 libxkbcommon-x11-0 -y

WORKDIR app
COPY src/requirements.txt .
RUN pip install -r requirements.txt