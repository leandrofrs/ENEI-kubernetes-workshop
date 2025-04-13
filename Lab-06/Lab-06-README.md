# Lab-06: Deploying with Helm

This lab demonstrates how to package and deploy the Flask app using Helm — Kubernetes' package manager.

---

## 📁 Directory Structure

- `flask-app/`: App source code.
- `charts/`: Helm chart directory.
  - `Chart.yaml`, `values.yaml`, `templates/`

---

## 📦 Kubernetes Features Highlighted

- ✅ Helm Chart
- ✅ Deployment
- ✅ PVC, ConfigMap, Secret
- ✅ HPA
- ✅ Probes


---

## 🧼 Pre-Deployment Cleanup

Before deploying with Helm, clean up resources created in Labs 01–05:

### Lab 05
```bash
kubectl delete -f ../Lab-05/deployment.yaml
```

### Lab 04
```bash
kubectl delete -f ../Lab-04/hpa.yaml
```

### Lab 03
```bash
kubectl delete -f ../Lab-03/pvc.yaml
kubectl delete -f ../Lab-03/pv.yaml
```

### Lab 02
```bash
kubectl delete -f ../Lab-02/config-map.yaml
kubectl delete -f ../Lab-02/secret.yaml
```

### Lab 01
```bash
kubectl delete -f ../Lab-01/service.yaml
```

---

## 🚀 Steps to Deploy

### 1. Install Helm (if needed)

Linux/MacOS:
```bash
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
```
Windows:
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
choco install kubernetes-helm
```

### 2. Create a Namespace

```bash
kubectl create namespace flask
```

### 3. Deploy with Helm

```bash
helm install flask-app flask-app --namespace flask
```

### 4. Verify

```bash
kubectl get all -n flask
```

---

## ✅ Outcome

You’ll have a full-featured Flask app deployed and managed with Helm.
