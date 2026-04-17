FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY project.ipynb .
COPY setup.py .
COPY README.md .

# Create models directory
RUN mkdir -p models

# Expose Jupyter port
EXPOSE 8888

# Expose API port (if using Flask)
EXPOSE 5000

# Default command: start Jupyter
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
