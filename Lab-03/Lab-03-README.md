# Lab-03: Deploying a Flask App with Persistent Storage

This lab demonstrates how to use PersistentVolumes (PV) and PersistentVolumeClaims (PVC) to persist data for a Flask application running on Kubernetes.

---

## 📁 Directory Structure

- `deployment.yaml`: Flask app deployment with volume mount.
- `pv.yaml`: Defines PersistentVolume.
- `pvc.yaml`: Defines PersistentVolumeClaim.
- `Flask-app/app.py`: Flask code writing to `/data/log.txt`.
- `Flask-app/Dockerfile`: Dockerfile to build the app image.
- `README.md`: Documentation.

---

## 📦 Kubernetes Features Highlighted

- ✅ Deployment
- ✅ PVC & PV

---

## 🚀 Steps to Deploy

### 1. Apply Storage Resources

Modify the `pv.yaml` with path to your host directory for persistent storage. For example:
Modify the `path` in the `hostPath` section of `pv.yaml` to point to your desired directory for persistent storage. For example:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
    name: flask-pv
spec:
    capacity:
        storage: 10Mi
    accessModes:
        - ReadWriteOnce
    storageClassName: manual
    hostPath:
        path: "/Users/leandro.f.sousa/Projects/kubernetes-workshop/Lab-03/flask-pv"
```
    
Then apply the PV and PVC:
```bash
kubectl apply -f pv.yaml
kubectl apply -f pvc.yaml
```

### 2. Build the Docker Image

```bash
cd Flask-app
docker build -t flask-app:1.0.3 .
```

### 3. Deploy the Application

```bash
kubectl apply -f deployment.yaml
```

### 4. Verify Deployment

```bash
kubectl get pods
kubectl get pvc
kubectl get pv
```

### 5. Access the Application
Get the NodePort and access the app via your browser:

```bash
kubectl get services
# Then use http://<node-ip>:<node-port>/log
```
### 6. Check Logs

```bash
kubectl exec -it <pod-name> -- cat /data/log.txt
```

check logs also on the host machine:
```bash
cat ./flask-pv/log.txt
```

---

## ✅ Outcome

App writes log data to a persistent volume. The logs survive pod restarts.
