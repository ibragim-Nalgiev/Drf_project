FROM python: 3.11

WORKDIR /Drf_project

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "Drf_project.py"]







