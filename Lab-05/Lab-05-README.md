# Lab-05: Probes - Ensuring App Health

This lab demonstrates how to configure readiness and liveness probes for a Flask application to ensure availability and self-healing.

---

## 📁 Directory Structure

- `deployment.yaml`: Deployment with health probes.
- `Flask-app/`: Application source code and Dockerfile.
- `README.md`: Documentation.

---

## 📦 Kubernetes Features Highlighted

- ✅ Readiness Probe
- ✅ Liveness Probe

---

## 🚀 Steps to Deploy

### 1. Apply Deployment

```bash
kubectl apply -f deployment.yaml
```

### 2. Verify Probe Configuration

```yaml
readinessProbe:
  httpGet:
    path: /
    port: 8000
  initialDelaySeconds: 5

livenessProbe:
  httpGet:
    path: /
    port: 8000
  initialDelaySeconds: 15
```

### 3. Check Pod Events

```bash
kubectl describe pod <pod-name>
```

### 4. Modify Probes to Simulate Failure

```yaml
readinessProbe:
  httpGet:
    path: /healthz
    port: 8000
  initialDelaySeconds: 5

livenessProbe:
  httpGet:
    path: /livenessz
    port: 8000
  initialDelaySeconds: 15
```

### 5. Apply Changes

```bash
kubectl apply -f deployment.yaml
```
### 6. Monitor Pod Status

```bash
kubectl get pods
```

```bash
kubectl describe pod <pod-name>
```

---

## ✅ Outcome

Pods will only serve traffic when ready, and will auto-restart if unhealthy.
