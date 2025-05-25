from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student data
with open('students.json') as f:
    students = json.load(f)

@app.get("/")
def root():
    return {"message": "Student Marks API is running"}

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist('name')
    marks = []
    for name in names:
        student = next((s for s in students if s['name'].lower() == name.lower()), None)
        marks.append(student['mark'] if student else None)
    return {"marks": marks}