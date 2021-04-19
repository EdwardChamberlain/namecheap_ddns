FROM python:3.8
COPY src/ /tmp/
RUN pip install requests
RUN export PYTHONUNBUFFERED=0
CMD ["python", "-u", "/tmp/main.py"]