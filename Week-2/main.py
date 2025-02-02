from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import Optional, List

# Create FastAPI app instance
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET"],  # Only allow GET requests
    allow_headers=["*"],
)

# Load student data
try:
    students_df = pd.read_csv("students.csv")
except FileNotFoundError:
    print("Warning: students.csv not found. API will return empty results.")
    students_df = pd.DataFrame(columns=['class'])

@app.get("/api")
async def get_students(
    class_filter: Optional[List[str]] = Query(None, alias="class")
):
    """
    Get students, optionally filtered by class.
    
    Parameters:
    - class_filter: Optional list of class names (e.g., ['1A', '1B'])
    
    Returns:
    - JSON object with list of students matching the filter criteria
    """
    # Apply class filter if provided
    if class_filter:
        filtered_df = students_df[students_df['class'].isin(class_filter)]
    else:
        filtered_df = students_df
    
    # Convert to list of dictionaries, preserving original order
    students_list = filtered_df.to_dict(orient='records')
    
    return {"students": students_list}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)