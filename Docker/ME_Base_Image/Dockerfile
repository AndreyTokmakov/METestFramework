FROM alpine:3.18
RUN apk update && \
    apk add --no-cache less cronie logrotate procps-ng psmisc cmake make wget bash build-base && \
    apk add --no-cache openssl curl-dev && \
    wget https://archive.apache.org/dist/pulsar/pulsar-client-cpp-3.5.1/apk-x86_64/x86_64/apache-pulsar-client-3.5.1-r0.apk && \
    wget https://archive.apache.org/dist/pulsar/pulsar-client-cpp-3.5.1/apk-x86_64/x86_64/apache-pulsar-client-dev-3.5.1-r0.apk && \
    apk add --allow-untrusted apache-pulsar-client-3.5.1-r0.apk && \
    apk add --allow-untrusted apache-pulsar-client-dev-3.5.1-r0.apk