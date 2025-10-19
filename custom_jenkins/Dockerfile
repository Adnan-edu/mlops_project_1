FROM jenkins/jenkins:lts

USER root

# --- Install system dependencies, Docker, Python ---
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        gnupg \
        python3 \
        python3-venv \
        python3-pip \
        git \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg \
        | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
        https://download.docker.com/linux/debian $(. /etc/os-release && echo $VERSION_CODENAME) stable" \
        > /etc/apt/sources.list.d/docker.list && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends docker-ce docker-ce-cli containerd.io && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# --- Install Docker Buildx ---
RUN mkdir -p ~/.docker/cli-plugins && \
    curl -SL https://github.com/docker/buildx/releases/latest/download/buildx-v0.10.5.linux-amd64 \
        -o ~/.docker/cli-plugins/docker-buildx && \
    chmod +x ~/.docker/cli-plugins/docker-buildx

# --- Add Jenkins user to docker group ---
RUN groupadd -f docker && usermod -aG docker jenkins

# --- DinD runtime mountpoint ---
VOLUME /var/lib/docker

# --- Start dockerd before Jenkins ---
ENTRYPOINT ["/bin/bash", "-c", "dockerd > /var/log/dockerd.log 2>&1 & exec /usr/local/bin/jenkins.sh"]

USER jenkins
