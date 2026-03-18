FROM python:3.9-slim
RUN pip install --progress-bar off flask
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY sample_app.py /home/myapp/
EXPOSE 5050
ENV STUDENT_TOKEN=D1-IB-23-5b-11-7A51
CMD python3 /home/myapp/sample_app.py
