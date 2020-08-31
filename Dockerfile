FROM python:3
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY snac ./snac
WORKDIR /snac
CMD ["python", "main.py"]