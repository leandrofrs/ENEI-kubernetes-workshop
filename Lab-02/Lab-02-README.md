# Lab-02: Managing Configuration with ConfigMaps and Secrets

This lab demonstrates how to use ConfigMaps and Secrets in Kubernetes to manage application configuration and sensitive data for a Flask application.

---

## 📁 Directory Structure

- `config-map.yaml`: Defines a ConfigMap for configuration.
- `secret.yaml`: Defines a Secret for sensitive data.
- `deployment.yaml`: Deployment using env vars from ConfigMap and Secret.
- `Flask-app/app.py`: Flask application code.
- `Flask-app/Dockerfile`: Dockerfile for the app.
- `README.md`: Documentation.

---

## 📦 Kubernetes Features Highlighted

- ✅ Deployment
- ✅ ConfigMap
- ✅ Secret

---

## 🚀 Steps to Deploy

### 1. Build the Docker Image

```bash
cd Flask-app
docker build -t flask-app:1.0.2 .
```

### 2. Apply ConfigMap and Secret

```bash
kubectl apply -f ../config-map.yaml
kubectl apply -f ../secret.yaml
```

### 3. Deploy the Application

```bash
kubectl apply -f ../deployment.yaml
```

### 4. Verify the Deployment

```bash
kubectl get deployments
kubectl get pods
```

### 5. Access the Application

Get the NodePort and access the app via your browser:

```bash
kubectl get services
# Then use http://<node-ip>:<node-port>
```

---

## 🔎 Application Variables

- `APP_NAME`: Set via ConfigMap
- `API_KEY`: Set via Secret


---

## ✅ Outcome

The application should load configuration values from a ConfigMap and a Secret injected as environment variables.
