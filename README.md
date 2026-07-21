# Global Forex Dashboard 📈

A real-time foreign exchange (Forex) rate analytics dashboard built using Python, Flask, Jinja2, and Tailwind CSS. The application connects to an external REST API to fetch live currency conversion rates against USD, processes the payload on a custom backend, and renders a sleek, responsive dark-mode UI.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=flat&logo=flask&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-3.0+-06B6D4?style=flat&logo=tailwindcss&logoColor=white)

---

## 🛠️ Tech Stack & Architecture

- **Backend Framework:** Python (Flask)
- **HTTP Client:** `requests` library (REST API integration)
- **Templating Engine:** Jinja2 (Dynamic UI interpolation)
- **Frontend Styling:** Tailwind CSS (Responsive Utility-First Layout)
- **Data Source:** ExchangeRate-API (Live Financial Data)

---

## ⚙️ How It Works (Data Flow)

1. **User Request:** Client accesses the application route (`/`).
2. **API Data Fetch:** Flask queries the ExchangeRate-API endpoint via `requests.get()`.
3. **Data Processing:** Python parses raw JSON data, rounds currency rates to clean decimals, and encapsulates execution inside `try/except` blocks for graceful failure handling.
4. **Server-Side Rendering:** Flask uses Jinja2 to dynamically inject market variables into `index.html`.
5. **UI Rendering:** Web browser renders a fully styled, dark-themed dashboard displaying live USD rates for GBP, EUR, and JPY.

---

## 🚀 Getting Started Locally

### Prerequisites
- Python 3.x installed
- Git installed

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/RiyaanAhmedSadiq/market-dashboard.git](https://github.com/RiyaanAhmedSadiq/market-dashboard.git)
   cd market-dashboard