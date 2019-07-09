FROM ahmad88me/pandas:22-python2.7-alpine
WORKDIR /app

RUN pip freeze
COPY templates /app/templates
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY *.py /app/
RUN mkdir -p local_uploads
CMD ["python", "app.py"]
