# 🔍 Smart Research Manager (Asynchronous Scraper & Data Manager)

### 📝 Project Description
An advanced Command Line Interface (CLI) research assistant built in Python. This tool automates educational research by simultaneously scraping data from **Wikipedia REST API** and **DuckDuckGo Search Engine** using asynchronous concurrency. It includes a complete local database management system with user login, data backup, analytics, and file export options.

### 🚀 Core Features
* **⚡ Asynchronous Concurrency:** Utilizes Python's `asyncio` and `gather` to fetch data from multiple web sources at the same time, significantly reducing wait times.
* **🌐 Web Scraping & API Integration:** Parses live HTML structures from search engine results using `BeautifulSoup4` and communicates with external REST APIs using `requests`.
* **🔒 Secure User Profiles:** Supports multiple local user accounts protected by an isolated PIN-authentication mapping system.
* **📊 Live Analytics & Statistics:** Features an integrated metrics logger that calculates total searches, success/failure rates, and distinct platform hits.
* **🔎 Deep Keyword Search:** Implements a custom recursive algorithm to scan through nested data layers and find user-specified phrases.
* **📁 Data Management (CRUD & Backup):**
  * **Export:** Convert and save structured JSON research into readable `.txt` report files.
  * **Delete:** Safely remove individual search records or wipe entire user accounts with binary prompt confirmation.
  * **Backup & Restore:** One-click automated database duplication to a secure backup directory to avoid accidental data loss.
  * **CLI Arguments:** Supports quick execution shortcuts using the `sys.argv` module.

### 🛠️ Tech Stack & Advanced Concepts Used
* **Language:** Python 3 (Optimized for Android via Pydroid 3)
* **Concurrency:** Asynchronous Event Loops (`asyncio`, tasks, coroutines)
* **Web Modules:** `BeautifulSoup4` (HTML parsing) and `requests` (HTTP requests)
* **Database & Storage:** `json` file serialization, stream data filtering, and OS file manipulation (`os.path`, `os.remove`, `os.listdir`).
* **Error Handling:** Bulletproof `try...except` handling for smooth operational loops.
