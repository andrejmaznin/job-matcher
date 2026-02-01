FROM ubuntu:latest
LABEL authors="andrejmaznin"

ENTRYPOINT ["top", "-b"]