<p align="center">
  <img src="weather.jpg" alt="Banner" width="50%" style="max-width:100%; height:auto;" />
</p>

## <h1 align="center">Heatmap Generator with Live Weather Tracker</h1>

This is a Django web application that allows users to generate customized heatmaps using Seaborn and NumPy, upload CSV files for heatmap visualization, and track current weather using real-time web scraping from [timeanddate.com](https://www.timeanddate.com/).

---

##  Features

###  Heatmap Generator
- **User-defined dimensions**: Set number of rows and columns.
- **Colormap selection**: Choose from coolwarm, viridis, plasma, and more.
- **CSV upload support**: Upload your own dataset to visualize.
- **Annotations**: Toggle value display inside heatmap cells.
- **Random seed**: Control reproducibility of generated data.
- **Download heatmap as PNG**.
- **Heatmap history**: Stores and displays last 5 generated heatmaps.
- Ready for **AJAX live updates** and **PDF export** (future enhancements).

### Weather Tracker
- Input country and city.
- Scrapes live weather data (temperature and description) from timeanddate.com.
- Includes country code mapping to ensure valid URL format.

---

## Getting Started

### Installation

# Clone the repository:
```
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

# Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
# Install dependencies:
```
pip install -r requirements.txt
```
# Apply migrations:
```
python manage.py migrate
```
# Run the development server:
```
python manage.py runserver
```
# Project Structure
```
seaborn_heatmap/
├── heatmap_app/
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/heatmap_app/
│       ├── heatmap.html
│       └── weather.html
├── seaborn_heatmap/
│   ├── settings.py
│   └── urls.py
├── static/
│   └── heatmap.png
├── db.sqlite3
├── manage.py
```
# Dependencies

- Django

- numpy

- matplotlib

- seaborn

- pandas

- requests

- beautifulsoup4

# Install them with:
```
pip install -r requirements.txt
```
# Future Improvements

- AJAX live heatmap preview

- PDF and ZIP export

- User authentication + saved dashboards

- Dark/light theme toggle

- Smart weather auto-suggestions

# Credits

Built with using Django by ***Md Rakibul Hassan***

CSE Undergraduate | Backend Developer | Robotics & IoT Enthusiast

🔗 [LinkedIn](https://www.linkedin.com/in/md-rakibul-hassan-507b00308)

🐙 [GitHub](https://github.com/RR0327)

Designed to help users better understand the emoji language.

# License

This project is open source and available under the MIT License.