from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from browser_use_sdk import BrowserUse
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="Small Business Hack API", version="1.0.0")

prompt = """
Sign in to dedaluslabs.ai and type the following email: vallerus55@gmail.com
Wait until new screen is loaded with dashboard button in the right corner
Click on Dashboard button in the top right corner
Click on Add server button in the top right corner
Select business-agent-template  and click configure server
Paste the following text in env variables: BUSINESS_KNOWLEDGE="I am a professional photographer in London, UK, capturing authentic moments with style. 📸 Services: Portraits, Events (weddings, corporate, parties), Commercial (products, headshots, lifestyle), Real estate shoots, Street photography workshops. 🕒 Hours: Weekends 9-5, Weekdays for consultations & editing, Emergency sessions with 24h notice. 📍 Coverage: Central, North, South, East & West London. 💰 Pricing: Portraits £150-300, Events £400-800, Commercial £200-500/day, Travel in London included, outside £0.50/mi. 📱 Contact: hello@londonphotographer.co.uk | +44 20 7123 4567 | www.londonphotographer.co.uk | IG @london_photographer_pro. 🎯 Specialties: Natural & studio light, retouching, editing, color grading, fast digital delivery (48-72h). Professional, friendly, client-focused service."
Click on Deploy the server button
"""

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/browser-agent")
async def run_browser_agent():
    try:
        # Initialize the BrowserUse client
        client = BrowserUse(api_key=os.getenv("BROWSER_USE_API_KEY"))
        
        # Create and run the task
        task = client.tasks.create_task(
            task=prompt,
            llm="gpt-4o-mini"
        )
        
        result = task.complete()
        
        return {
            "status": "success",
            "task": prompt,
            "output": result.output,
            "message": "Browser agent completed successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error running browser agent: {str(e)}")
