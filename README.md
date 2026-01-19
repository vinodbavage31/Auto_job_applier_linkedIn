# LinkedIn Auto Job Applier (Stable Local Version) 🤖

This project is a **Python-based automation tool** that helps apply to LinkedIn jobs using the Easy Apply feature.

⚠️ **This repository is intended for LOCAL USE ONLY.**  
There is **no backend API or frontend UI required** to use this version.

This version focuses on:
- Stability
- Clear setup
- Predictable behavior
- Manual control

---

## 🚀 What This Bot Does

- Searches LinkedIn jobs based on your preferences
- Automatically fills Easy Apply forms
- Uploads your resume
- Answers common application questions
- Applies to jobs in bulk
- Supports **DRY RUN mode** for safe testing

---

## ⚠️ IMPORTANT BEFORE YOU START (READ THIS)

This bot:
- **Controls your browser**
- **Opens Chrome automatically**
- **Requires your screen to stay ON**
- **May be blocked by LinkedIn if abused**

👉 Always start with **DRY RUN mode**  
👉 Use responsibly and at your own risk

---

## 🧰 System Requirements

- **OS**: Windows (recommended)
- **Python**: 3.9 – 3.11 (⚠️ Python 3.13+ is NOT recommended)
- **Browser**: Google Chrome (latest)
- **Internet**: Stable connection
- **Display**: Screen must stay active

---

## 📦 Installation (Step-by-Step)

### 1️⃣ Install Python
Download and install Python from:
https://www.python.org/downloads/

✅ During installation, **check**:

Verify:
```bash
python --version
pip --version
```

- Clone the Repository
```
git clone <your-github-repo-url>
cd Auto_job_applier_linkedIn
```
- Install Dependencies
```pip install -r requirements.txt
```
- If requirements.txt is missing:
```
pip install undetected-chromedriver pyautogui selenium openai
```


#### install Google Chrome

- Download and install Chrome from:
```
https://www.google.com/chrome
```
#### How to Run the Bot (Correct Way)
FIRST RUN (Safe Mode)
```
python runAiBot.py --dry-run
```
#### REAL APPLICATION MODE (Use Carefully)
```
python runAiBot.py --real-apply
```
#### How to Stop the Bot

- Press CTRL + C in the terminal

- Or close the Chrome window manually