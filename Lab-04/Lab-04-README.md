# Lab-04: Auto-Scaling with Horizontal Pod Autoscaler

This lab shows how to set up Kubernetes' Horizontal Pod Autoscaler (HPA) to automatically scale a Flask app based on CPU usage.

---

## 📁 Directory Structure

- `deployment.yaml`: Includes CPU requests/limits.
- `hpa.yaml`: Defines the HPA object.
- `metric-server.yaml`: (optional) to deploy metrics server.
- `README.md`: Documentation.

---

## 📦 Kubernetes Features Highlighted

- ✅ HPA
- ✅ Metrics Server

---

## 🚀 Steps to Deploy

### 1. Deploy Metrics Server (if not installed)

```bash
kubectl apply -f metric-server.yaml
```

### 2. Apply Deployment and HPA

```bash
kubectl apply -f deployment.yaml
kubectl apply -f hpa.yaml
```

### 3. Simulate Load

```bash
kubectl run -i --tty load-generator --image=busybox -- /bin/sh
```
```bash
while true; do wget -q -O- http://<flask-app-ip>:<port>/; done
```

### 4. Monitor HPA

```bash
kubectl get hpa
```

---

## ✅ Outcome

The number of pods should scale up/down based on the load.
