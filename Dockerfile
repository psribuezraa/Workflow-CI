FROM python:3.10-slim
WORKDIR /app
COPY MLProject/ .
RUN pip install mlflow pandas scikit-learn
ENTRYPOINT ["python", "modelling.py"]