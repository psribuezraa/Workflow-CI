# Workflow-CI: MLflow Project dengan GitHub Actions

Repository ini berisi MLflow Project untuk training model Telco Customer Churn dengan CI/CD Pipeline menggunakan GitHub Actions.

## 📁 Struktur Folder

```
3. Workflow-CI/
├── .github/
│   └── workflows/
│       └── ci-training.yml      # GitHub Actions workflow
├── MLProject/
│   ├── modelling.py             # Script training (CLI-enabled)
│   ├── conda.yaml               # Conda environment
│   ├── MLProject                # MLflow Project config
│   ├── preprocessed_data.csv    # Dataset
│   └── DOCKERHUB_LINK.md        # Link ke Docker Hub
├── Dockerfile                   # Docker configuration
└── README.md                    # Dokumentasi ini
```

## 🚀 Cara Menggunakan

### 1. Setup GitHub Secrets

Untuk mengaktifkan Docker Hub push, tambahkan secrets berikut di repository GitHub:

| Secret Name | Value |
|-------------|-------|
| `DOCKERHUB_USERNAME` | Username Docker Hub Anda |
| `DOCKERHUB_TOKEN` | Access Token dari Docker Hub |

**Cara membuat Docker Hub Token:**
1. Login ke [Docker Hub](https://hub.docker.com)
2. Pergi ke Account Settings → Security
3. Klik "New Access Token"
4. Copy token dan simpan sebagai GitHub Secret

### 2. Push ke GitHub

```bash
# Initialize git (jika belum)
git init

# Add remote
git remote add origin https://github.com/USERNAME/REPO.git

# Push
git add .
git commit -m "Initial commit"
git push -u origin main
```

### 3. Trigger Workflow

Workflow akan otomatis berjalan ketika:
- Ada push ke branch `main` dengan perubahan di folder `MLProject/`
- Manual trigger dari tab Actions di GitHub

### 4. Manual Trigger dengan Custom Parameters

1. Buka tab **Actions** di repository GitHub
2. Pilih workflow **CI Training Pipeline**
3. Klik **Run workflow**
4. Isi parameter:
   - `n_estimators`: Jumlah trees (default: 100)
   - `max_depth`: Kedalaman maksimum (default: 10)
5. Klik **Run workflow**

## 📊 Fitur CI/CD Pipeline

| Level | Fitur | Status |
|-------|-------|--------|
| Basic | MLProject folder ✓ | ✅ |
| Basic | CI Workflow trigger training | ✅ |
| Skilled | Save artifacts ke GitHub | ✅ |
| Advance | Docker image ke Docker Hub | ✅ |

### Job dalam Workflow:

1. **train**: Menjalankan training dan upload artifacts
2. **build-docker**: Build dan push Docker image ke Docker Hub
3. **commit-artifacts**: Commit artifacts ke repository

## 🐳 Docker Image

Setelah workflow berjalan, Docker image akan tersedia di:

```
ezrapsribu/telco-churn-model:latest
```

### Pull dan Run:

```bash
docker pull ezrapsribu/telco-churn-model:latest
docker run -p 5000:5000 ezrapsribu/telco-churn-model:latest
```

## 📝 Local Testing

Untuk test MLflow Project secara lokal:

```bash
cd MLProject

# Install dependencies
pip install mlflow pandas scikit-learn

# Run dengan default parameters
python modelling.py

# Run dengan custom parameters
python modelling.py --n_estimators 50 --max_depth 5
```

## 👤 Author

**Ezra Abhinaya Pasaribu**  
Docker Hub: [ezrapsribu](https://hub.docker.com/u/ezrapsribu)
