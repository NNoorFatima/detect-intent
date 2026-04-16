from fastapi import FastAPI
from pydantic import BaseModel
from detect_intent import detect_intent

# Initialize the FastAPI app
app = FastAPI(title="AIVA Bot Intent Detection API")

# Define the expected format of the incoming request
class UserMessage(BaseModel):
    message: str

# Create a POST endpoint at /detect
@app.post("/detect")
def detect_user_intent(request: UserMessage):
    """
    Takes a JSON payload with a 'message' string, passes it to detect_intent(),
    and returns the resulting intent JSON.
    """
    # Call your exact function from detect_intent.py
    result = detect_intent(request.message)
    return result

# Optional: A simple health check endpoint
@app.get("/")
def read_root():
    return {"status": "API is running!"}

if __name__ == "__main__":
    import uvicorn
    # Change 3000 to whatever port you prefer
    uvicorn.run(app, host="0.0.0.0", port=3000)