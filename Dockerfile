FROM python:3.8

WORKDIR /app

CMD ["sudo", "apt-get", "install", "python3-tk"]
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install Pillow opencv-python tensorflow

ADD phone-webcam-detector.py phone-webcam-detector.py
ADD model.h5 model.h5

CMD ["python3", "phone-webcam-detector.py"]
