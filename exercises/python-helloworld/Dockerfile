FROM python:alpine3.17
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apk update && apk upgrade && apk add bash
EXPOSE 5000
CMD ["waitress-serve", "--port", "5000", "--call", "app:create_app"]