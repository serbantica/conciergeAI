import os

# Define the simplified structure of the project
project_structure = {
    'AI-Concierge-Project': {
        'agents': [
            '__init__.py',
            'knowledge_agent.py',
            'wellbeing_agent.py',
            'planning_agent.py',
            'nutrition_agent.py',
            'personal_dev_agent.py'
        ],
        'api': {
            '__init__.py': None,
            'main.py': """from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Concierge AI Assistant!"}
            """,
            'endpoints': {
                'knowledge.py': """from fastapi import APIRouter

router = APIRouter()

@router.get("/knowledge/")
def get_knowledge():
    return {"message": "Knowledge area accessed!"}
                """,
                'wellbeing.py': """from fastapi import APIRouter

router = APIRouter()

@router.get("/wellbeing/")
def get_wellbeing():
    return {"message": "Wellbeing area accessed!"}
                """,
                'planning.py': """from fastapi import APIRouter

router = APIRouter()

@router.get("/planning/")
def get_planning():
    return {"message": "Planning area accessed!"}
                """,
                'nutrition.py': """from fastapi import APIRouter

router = APIRouter()

@router.get("/nutrition/")
def get_nutrition():
    return {"message": "Nutrition area accessed!"}
                """,
            },
            'models': {
                'user.py': """from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
                """,
                'query.py': """from pydantic import BaseModel

class Query(BaseModel):
    question: str
                """
            }
        },
        'services': [
            '__init__.py',
            'celery_tasks.py',
            'message_queue.py'
        ],
        'databases': [
            '__init__.py',
            'postgres.py',
            'vector_db.py'
        ],
        'config': [
            '__init__.py',
            'settings.py',
            'config.yaml'
        ],
        'logs': [
            'app.log',
            'errors.log'
        ],
        'requirements.txt': """fastapi==0.85.1
celery==5.2.3
langchain==0.0.126
pydantic==1.10.5
uvicorn==0.19.0
postgresql==2.10.0
pika==1.2.0
pinecone-client==2.0.1
        """,
        'Dockerfile': """# Dockerfile for Concierge AI Assistant

FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
        """,
        'docker-compose.yml': """version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    command: ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
  rabbitmq:
    image: "rabbitmq:management"
    ports:
      - "15672:15672"
      - "5672:5672"
        """,
        'README.md': """# Concierge AI Assistant

This is a project to build a comprehensive AI Assistant with various capabilities:
- Personal development
- Wellbeing
- Knowledge management
- And more!

## Setup
1. Install dependencies with `pip install -r requirements.txt`
2. Run the FastAPI app with `uvicorn api.main:app --reload`
3. Start the Celery worker with `celery -A services.celery_tasks worker --loglevel=info`
4. Set up RabbitMQ with Docker
        """,
        '.env': """# Environment variables for the project
DATABASE_URL=your_database_url
RABBITMQ_URL=your_rabbitmq_url
API_KEY=your_api_key
        """
    }
}

# Helper function to create directories and files
def create_project_structure(base_path, structure):
    for name, value in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(value, dict):
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, value)
        elif isinstance(value, list):
            os.makedirs(path, exist_ok=True)
            for file in value:
                with open(os.path.join(path, file), 'w') as f:
                    # Check for content and provide placeholder if None
                    if value is None:
                        f.write(f"# Placeholder for {file}")
                    elif file.endswith('.py'):
                        f.write("# Placeholder for Python file\n")
                    elif file == 'requirements.txt':
                        f.write(value)
                    elif file == 'Dockerfile':
                        f.write(value)
                    elif file == 'docker-compose.yml':
                        f.write(value)
                    elif file == 'README.md':
                        f.write(value)
                    elif file == '.env':
                        f.write(value)
        else:
            with open(path, 'w') as f:
                # Check for content and provide placeholder if None
                if value is None:
                    f.write("# Placeholder content for " + name)
                else:
                    f.write(value)

# Specify the project base path and create the structure
base_path = r"C:\Users\ZZ029K826\Documents\GitHub"
create_project_structure(base_path, project_structure)
print(f"Project structure created at {base_path}")
