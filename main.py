from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="Egypt Urban Code Agent")

class Project(BaseModel):
    project_name: str
    city: Optional[str] = None
    authority: Optional[str] = None
    project_type: Optional[str] = None
    land_area_sqm: Optional[float] = None

projects = {}

@app.get("/")
def home():
    return {"service": "Egypt Urban Code Agent", "status": "running"}

@app.post("/projects")
def create_project(project: Project):
    pid = len(projects) + 1
    projects[pid] = project
    return {"project_id": pid, "project": project}

@app.get("/projects")
def list_projects():
    return projects

@app.get("/projects/{project_id}")
def get_project(project_id: int):
    return projects.get(project_id, "Not found")

@app.get("/report/{project_id}")
def generate_report(project_id: int):
    p = projects.get(project_id)
    if not p:
        return {"error": "project not found"}

    return {
        "executive_result": "Review required",
        "project": p,
        "checks": [
            {
                "topic": "Density",
                "status": "Needs authority confirmation"
            },
            {
                "topic": "Road hierarchy",
                "status": "Needs design review"
            },
            {
                "topic": "Parking",
                "status": "Not verified from source"
            }
        ]
    }
