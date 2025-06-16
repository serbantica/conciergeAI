# Concierge AI Assistant

This is a project to build a comprehensive AI Assistant with various capabilities:
- Personal development
- Wellbeing
- Knowledge management
- And more!

## Setup
1. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
2. Install dependencies with `pip install -r requirements.txt`
3. Set up RabbitMQ with Docker
4. Run the FastAPI app with `uvicorn api.main:app --reload`
5. Start the Celery worker with `celery -A services.celery_tasks worker --loglevel=info`
        