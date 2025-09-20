from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from browser_use_sdk import BrowserUse
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="Small Business Hack API", version="1.0.0")

class TaskRequest(BaseModel):
    task: str

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/browser-agent")
async def run_browser_agent(request: TaskRequest):
    try:
        # Initialize the BrowserUse client
        client = BrowserUse(api_key=os.getenv("BROWSER_USE_API_KEY"))
        
        # Create and run the task
        task = client.tasks.create_task(
            task=request.task,
            llm="gpt-4o-mini"
        )
        
        result = task.complete()
        
        return {
            "status": "success",
            "task": request.task,
            "output": result.output,
            "message": "Browser agent completed successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error running browser agent: {str(e)}")
