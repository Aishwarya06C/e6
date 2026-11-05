# Use a slim Debian base that supports multi-runtime setups
FROM openjdk:8-jdk-slim

# Install Python, curl, and required dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    unzip \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome for automated headless operations
RUN curl -LO https://google.com \
    && apt-get update && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb

# Setup Python Selenium dependencies
RUN pip3 install selenium webdriver-manager --break-system-packages || pip3 install selenium webdriver-manager

# Establish framework workspace
WORKDIR /app
COPY . /app

# Run tests via Maven wrapper or installed standard build environment tooling
CMD ["mvn", "clean", "test"]
