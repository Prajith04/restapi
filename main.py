from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date,time
app= FastAPI()
class Reminder(BaseModel):
    date:date
    time:time
    message:str
@app.post("/reminder")
def create_reminder(reminder: Reminder):
    return {"message": f"Reminder created for {reminder.date} at {reminder.time}: {reminder.message}"}
