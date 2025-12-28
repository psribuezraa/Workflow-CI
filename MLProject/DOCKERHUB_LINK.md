# Docker Hub Link

## Repository Docker Hub

**Image URL**: https://hub.docker.com/r/ezrapsribu/telco-churn-model

## Pull Image

```bash
docker pull ezrapsribu/telco-churn-model:latest
```

## Run Container

```bash
# Run model server
docker run -p 5000:5000 ezrapsribu/telco-churn-model:latest

# Kirim prediction request
curl -X POST http://localhost:5000/invocations \
  -H "Content-Type: application/json" \
  -d '{"columns": [...], "data": [[...]]}'
```

## Note

Image akan tersedia setelah workflow CI pertama kali berjalan di GitHub Actions dan berhasil push ke Docker Hub.

**Prerequisite GitHub Secrets:**
- `DOCKERHUB_USERNAME`: Username Docker Hub (ezrapsribu)
- `DOCKERHUB_TOKEN`: Access Token dari Docker Hub
