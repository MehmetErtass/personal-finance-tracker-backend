# 💰 Personal Finance Tracker – Backend

This is the backend of a Personal Finance Tracker built with Flask. It enables users to manage income and expenses, track their financial activity, and receive smart AI-based budgeting suggestions.

## 🚀 Features

- 📥 Add, update, and delete income and expenses
- 🧾 Categorize transactions 
- 🤖 Receive AI-powered budgeting suggestions 
- 📈 Track spending habits over time
- 🔒 Secure API endpoints using API keys
- 🌐 Ready to integrate with a frontend or mobile app

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python     | Core backend language |
| Flask      | Web framework |
| SQLAlchemy | ORM for database interactions |
| SQLite     | Lightweight relational database |
| OpenAI API | AI budget assistant |
| python-dotenv     | Manages .env configuration |

## 📁 Project Structure
```
personal-finance-tracker-backend/
│
├── app.py              # Main application file
├── config.py           # Configuration settings
├── routes.py           # API route definitions
├── models.py           # Database models
├── ai_model.py         # AI-based budget advisor logic
├── requirements.txt    # Project dependencies
├── .env                # Environment variables
│
├── templates/          # HTML templates
└── __pycache__/        # Python bytecode cache 
```

## 🔐 Environment Configuration

Create a `.env` file in the project root with the following content:
```
OPENAI_API_KEY=your_openai_api_key
SECRET_KEY=your_flask_secret_key
DATABASE_URL=postgresql://tracker_user:strongpassword123@localhost:5432/financial_tracker
PORT=5000
```
⚠️ Replace placeholder values with your actual credentials.


## 🧪 Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone https://github.com/MehmetErtass/personal-finance-tracker-backend.git
   cd personal-finance-tracker-backend

2. **(Optional) Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate 

3. **Activate the virtual environment:**

   Windows:
   ```
   venv\Scripts\activate
   ```
   macOS/Linux:
   ```bash
   source venv/bin/activate
   
   
  4. **Install dependencies:**
     ```bash
     pip install -r requirements.txt
  
  5. **Run the application:**
     ```
     python app.py
     ```
     The API will be available at:
      ```bash
      http://127.0.0.1:5000/

## 📬 API Endpoints
  |Endpoint | Method | Description |
  |------------|---------|---------|
  | add-income     | POST | Income data |
  | add-expense      | POST | Expense data |
  | get-transaction | GET | Retrieve all transactions |
  | ai-suggestion    | POST | Get AI-based budget suggestions |

## 🤖 AI Integration
The application uses OpenAI's GPT API to analyze transaction data and suggest personalized budgeting improvements. This feature helps users:
- Optimize monthly expenses
- Get tailored saving strategies
- Detect spending anomalies

## 📌 Future Improvements
* ✅ User authentication and session support
* ⏳ CSV export and import functionality
* ⏳ Integration with third-party bank APIs
* ⏳ Monthly & weekly financial reports
* ⏳ Unit testing and CI/CD setup

## 📝 License
This project is licensed under the MIT License.

Feel free to use, contribute, or fork the repository.
