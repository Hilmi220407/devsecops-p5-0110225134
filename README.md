# DevSecOps P5 - To-Do API

## 1. Nama Aplikasi & Fungsi
To-Do API adalah aplikasi web sederhana untuk mencatat, melihat,
dan menandai selesai tugas harian melalui REST API.

## 2. Bahasa / Framework
- Python 3.11
- Flask (web framework)
- Pytest (unit testing)
- Bandit (SAST tool)

## 3. Cara Menjalankan
```bash
git clone https://github.com/Hilmi220407/devsecops-p5-0110225134.git
cd devsecops-p5-NIM
pip install -r requirements.txt
python -m app.main
```
Aplikasi berjalan di http://127.0.0.1:5000/tasks

Menjalankan test: `python -m pytest`

## 4. Overview Pipeline CI/CD
Pipeline GitHub Actions (`.github/workflows/devsecops.yml`) terpicu saat
push dan pull request ke branch `main`, terdiri dari:
- **build**: install dependency dan menjalankan unit test
- **sast-scan**: scan keamanan kode dengan Bandit (bergantung pada job build)
