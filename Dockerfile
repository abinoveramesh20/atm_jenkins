# Build Stage
FROM python:3.8 AS build-stage

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Runtime Stage
FROM nginx:alpine

COPY --from=build-stage /app/build /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]

