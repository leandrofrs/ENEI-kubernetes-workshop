# Lab-01: Deploying a Flask Application on Kubernetes

This lab demonstrates how to deploy a simple Flask application on Kubernetes using a Deployment and a Service.

---

## 📁 Directory Structure

- `deployment.yaml`: Kubernetes Deployment for the Flask app.
- `service.yaml`: NodePort Service to expose the app.
- `Flask-app/app.py`: Flask application code.
- `Flask-app/Dockerfile`: Dockerfile for building the app image.
- `README.md`: Documentation.

---

## 📦 Kubernetes Features Highlighted

- ✅ Deployment
- ✅ Service (NodePort)

---

## 🚀 Steps to Deploy

### 1. Build the Docker Image

```bash
cd Flask-app
docker build -t flask-app:1.0.1 .
```

### 2. Deploy the Application

```bash
kubectl apply -f ../deployment.yaml
kubectl apply -f ../service.yaml
```

### 3. Verify the Deployment

```bash
kubectl get deployments
kubectl get pods
```

### 4. Access the Application

Get the NodePort and access the app via your browser:

```bash
kubectl get services
# Then use http://<node-ip>:<node-port>
```

---

## ✅ Outcome

You will have a Flask application running inside Kubernetes and exposed via a NodePort service.
