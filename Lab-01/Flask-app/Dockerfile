FROM python:3.10-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
EXPOSE 8000
CMD ["sh", "-c", "if [ -f /app/app.py ]; then python /app/app.py; else echo 'Error: /app/app.py not found'; exit 1; fi"]