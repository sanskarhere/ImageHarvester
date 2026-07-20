 <mark> <h1>📸 <i>Image Scraper — Automate  Image Collection</i></h1> </mark>

What if collecting hundreds of images from Google was as simple as typing a keyword and clicking a button?

**Image Scraper** is a Streamlit-based web app that automates image scraping from Google,Flipkart,meesho web app. Designed for developers, researchers, and creators who need fast access to visual data—without the manual grind.

---

## 🚀 Why 

Manual image collection is slow, repetitive, and error-prone. Whether you're training a machine learning model, designing a UI, or building a dataset—this tool saves time and sanity by automating the entire process. “Search. Scrape. Save. Simplified.”

---

## ✨ Features
- Developed a simple Streamlit UI  To Search Term 🔍 and Download  Image Folder
- Selected Selenium only for JavaScript-rendered pages.
- Implemented both browser automation and HTTP-based scraping.
- Used Requests for faster scraping where direct HTTP access was sufficient.
- Built a modular scraper architecture, making new platforms easy to integrate.
- Developed a simple Streamlit UI for an end-to-end scraping workflow.
- 📁 Saves all images into a structured local folder  and allow downloading it 

---

## 🛠️ Tech Stack

| Layer        | Tools Used                      |
|--------------|---------------------------------|
| Frontend     | Streamlit                       |
| Backend      | Python                          |
| Scraping     | BeautifulSoup,Requests,Selenium |
| Deployment   | Localhost (Prototype Phase)     |
|Browser Automation | ChromeDriver               |

---


## 📦 Installation

```bash
git clone https://github.com/sanskarhere/ImageHarvestor.git
cd ImageHarvestor
pip install -r requirements.txt
python app.py
