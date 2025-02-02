FAQ Management API (Django + REST Framework)
This is a Django-based backend application for managing FAQs with multilingual support. It includes:

✅ WYSIWYG Editor (for rich text formatting)
✅ REST API (to fetch FAQs in different languages)
✅ Caching with Redis (for performance optimization)
✅ Google Translate API (for auto-translations)
✅ Admin Panel (for managing FAQs)
✅ Unit Tests (to ensure quality)
🚀 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/faq-management-api.git
cd faq-management-api
2️⃣ Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv venv  
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Configure Environment Variables
Create a .env file in the project root and add:

ini
Copy
Edit
SECRET_KEY=your_secret_key  
DEBUG=True  
GOOGLE_TRANSLATE_API_KEY=your_api_key  
REDIS_URL=redis://localhost:6379/0  
5️⃣ Run Database Migrations
bash
Copy
Edit
python manage.py migrate
6️⃣ Create a Superuser (For Admin Panel Access)
bash
Copy
Edit
python manage.py createsuperuser
7️⃣ Start Redis (If Not Running)
bash
Copy
Edit
redis-server  # Linux/macOS
8️⃣ Run the Django Development Server
bash
Copy
Edit
python manage.py runserver
📌 API Usage
🌍 Get FAQs (With Language Support)
Endpoint:

http
Copy
Edit
GET /api/faqs/?lang=en
Response:

json
Copy
Edit
[
  {
    "id": 1,
    "question": "What is this API?",
    "answer": "This API manages FAQs with multilingual support."
  }
]
Available Languages: en (English), hi (Hindi), tg (Telugu)

📂 Project Structure
csharp
Copy
Edit
faq_management/
│── faqs/                # FAQ app (Models, Views, Serializers)
│── config/              # Django project settings
│── templates/           # HTML templates (if any)
│── static/              # Static files (CSS, JS)
│── manage.py            # Django CLI
│── requirements.txt     # Project dependencies
└── README.md            # Project documentation
✅ Running Tests
To run all unit tests:

bash
Copy
Edit
python manage.py test
🔗 API Documentation
Once the server is running, access API docs here:

Swagger UI: http://127.0.0.1:8000/api/docs/swagger/
ReDoc: http://127.0.0.1:8000/api/docs/redoc/
📜 License
This project is open-source and available under the MIT License.

🙌 Contributors
Manikanta Allena – Backend Development
