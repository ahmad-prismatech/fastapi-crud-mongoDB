from fastapi import FastAPI
from routes.todo_routes import todo_api_router

app = FastAPI()

@app.get('/')
async def initial_route():
    return{
        "status": "200",
        "message": "Initial route running"
    }

app.include_router(todo_api_router)