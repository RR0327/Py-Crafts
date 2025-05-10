<!-- Full-width high-quality image -->
<p align="center">
  <img src="bg-home.jpg" alt="Banner" width="50%" style="max-width:100%; height:auto;" />
</p>

# <h1 align="center">😎 EmojiPower — Emoji Meaning Extractor</h1>

**EmojiPower** is a fun, lightweight Django web application that helps users understand the meanings of emojis.  
It includes features like emoji meaning extraction, usage tracking, history logging, top-used emojis display, and downloadable results — all built with **pure Django, HTML, and CSS** (no JavaScript!).

---

## ✨ Key Features

- Extract emoji meanings using `demoji`
- Track emoji input history via Django sessions
- Display Top 5 most-used emojis
- Categorize emojis (e.g., ❤️ → Love, 😂 → Laugh)
- Random helpful emoji usage tips
- Download emoji analysis as `.txt`
- Different background images per page
- Fully responsive professional UI
- Pure Django + HTML + CSS (no JS!)
- Static file support via WhiteNoise for production

---

## 🌐 Page Routes & Structure

| Page         | URL path       | Purpose                             |
|--------------|----------------|-------------------------------------|
| 🏠 Home       | `/`            | Input emojis & view meanings        |
| 🕓 History    | `/history/`    | View past emoji inputs (session)    |
| 📈 Top Emojis | `/top/`        | Shows most frequently used emojis   |
| ℹ️ About       | `/about/`      | Info about the project              |
| ⬇ Download    | `/download/`   | Download emoji analysis result      |

Each route has its **own background image**, unique layout, and clean styling.

---

## 🛠️ Technologies Used

- Python 3.9+
- Django 5.2
- Demoji (for emoji parsing)
- WhiteNoise (for static files)
- HTML5 + CSS3

---

## 📦 Project Structure

Emoji_Meaning_Extractor/
│
├── emoji_app/
│ ├── views.py
│ ├── urls.py
│ ├── templates/emoji_app/
│ │ ├── home.html
│ │ ├── history.html
│ │ ├── top.html
│ │ ├── about.html
│ │ └── navbar.html
│ ├── static/emoji_app/
│ │ ├── bg-home.jpg
│ │ ├── bg-other.jpg
│ │ └── styles.css
│ └── templatetags/dict_filters.py
│
├── emoji_project/
│ ├── settings.py
│ ├── urls.py
│
├── requirements.txt
├── .gitignore
├── README.md
└── manage.py
---

## 🧪 Local Development Setup

```
# Clone the repository
git clone https://github.com/RR0327/emoji-power.git
cd emoji-power
```

# Create and activate virtual environment
```
python -m venv venv
venv\Scripts\activate  # On macOS/Linux: source venv/bin/activate
```

# Install dependencies
```
pip install -r requirements.txt
```

# Run migrations and start server
```
python manage.py migrate
python manage.py runserver
```

# Collect Static Files (for production)
```
python manage.py collectstatic
```
# • WhiteNoise will serve static files from /staticfiles/ in production.

🌍 Deployment Ready

The project is prepared for deployment with:

✅ WhiteNoise middleware

✅ STATIC_ROOT and STATICFILES_STORAGE settings

✅ .gitignore and requirements.txt ready

Easily deployable to platforms like Render, Heroku, or PythonAnywhere.

🙌 Credits

Built with using Django by Md Rakibul Hassan

Designed to help users better understand the emoji language.

📄 License

This project is open source and available under the MIT License.
