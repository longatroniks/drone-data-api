
# Axpo Drone Data API

This project provides a simple REST API to serve asset data (e.g. substations, run-of-river plants) from a CSV file. It is built using **Flask**, containerized using **Docker**, and deployed on **Vercel**.


## 📦 Features

- Serves a CSV dataset as a JSON API
- Built with Flask and Gunicorn
- Dockerized for portability
- Deployed with Vercel's custom Docker runtime
- CORS-enabled for frontend integration


## 🔧 Tech Stack

- Python 3.11
- Flask
- Gunicorn
- Docker
- Vercel (for deployment)


## 🚀 Live Demo

**Production URL:**  
👉 [https://your-vercel-domain.vercel.app/api/assets](https://your-vercel-domain.vercel.app/api/assets)

> *(Replace with your actual deployed URL after Vercel deployment)*


## 📁 Project Structure

```
axpo-drone-data-api/
├── app.py              # Flask app
├── assets.csv          # Asset data file
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker config for production
├── .dockerignore       # Excludes files from Docker image
├── vercel.json         # Vercel config for Docker runtime
└── README.md
```


## ⚙️ Getting Started Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/axpo-drone-data-api.git
cd axpo-drone-data-api
```

### 2. Run with Docker

```bash
docker build -t drone-api .
docker run -p 5000:5000 drone-api
```

### 3. Test locally

Visit: [http://localhost:5000/api/assets](http://localhost:5000/api/assets)


## ☁️ Deploying to Vercel

### 1. Install the Vercel CLI

```bash
npm install -g vercel
```

### 2. Log in and deploy

```bash
vercel login
vercel --prod
```

Vercel will detect the `Dockerfile` and deploy it as a container.


## 🔄 API Endpoint

### `GET /api/assets`

Returns a list of all assets with metadata.

#### Sample response:

```json
[
  {
    "id": "VL35",
    "name": "Glovelier",
    "type": "run-of-river",
    "latitude": 46.105880590640965,
    "longitude": 7.809260581732722
  },
  ...
]
```

