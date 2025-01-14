ARG PORT=443
FROM cypress/browsers:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/venv

COPY requirements.txt .
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

RUN /opt/venv/bin/pip install --ignore-installed uvicorn==0.20.0

ENV PATH="/opt/venv/bin:$PATH"

CMD gunicorn app:app --bind 0.0.0.0:$PORT --timeout 0
