FROM jenkins/jenkins:lts

USER root

# --- Install Docker Engine (client + daemon) properly ---
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ca-certificates curl gnupg && \
    install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg \
        | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
        https://download.docker.com/linux/debian $(. /etc/os-release && echo $VERSION_CODENAME) stable" \
        > /etc/apt/sources.list.d/docker.list && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends docker-ce docker-ce-cli containerd.io && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# --- Add Jenkins user to docker group ---
RUN groupadd -f docker && usermod -aG docker jenkins

# --- DinD runtime mountpoint ---
VOLUME /var/lib/docker

# --- Start dockerd before Jenkins ---
# dockerd runs in background, then exec Jenkins entrypoint
ENTRYPOINT ["/bin/bash", "-c", "dockerd > /var/log/dockerd.log 2>&1 & exec /usr/local/bin/jenkins.sh"]

USER jenkins
