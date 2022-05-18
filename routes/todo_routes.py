from logging import raiseExceptions
from fastapi import APIRouter
from config.database import collection_name
from models.todo_model import Todo
from schemas.todo_schema import todo_serializer, todos_serializer
from bson.objectid import ObjectId
import json
from fastapi import HTTPException
from service.responses import success_response, error_response, onlySuccessResponseWithoutData

todo_api_router = APIRouter()

# retrieve
@todo_api_router.get("/todos")
async def get_todos():
    todos = todos_serializer(collection_name.find())
    result = success_response(200,"Success", todos)
    return result

# single todo
@todo_api_router.get("/{id}")
async def get_todo(id: str):
    todo = todo_serializer(collection_name.find_one({"_id": ObjectId(id)}))
    result = success_response(200,"Success", todo)
    return result

# create todo
@todo_api_router.post("/")
async def post_todo(todo: Todo):
    _id = collection_name.insert_one(dict(todo))
    todo = todo_serializer(
    collection_name.find_one({"_id": _id.inserted_id}))    
    result = success_response(200,"Success", todo)
    return result

# update todo
@todo_api_router.put("/{id}")
async def update_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(todo)
    })
    updated_todo = todo_serializer(collection_name.find_one({"_id":ObjectId(id)}))
    result = success_response(200,"Success", updated_todo)
    return result

# delete todo
@todo_api_router.delete("/{id}")
async def delete_todo(id: str, todo: Todo):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    result = onlySuccessResponseWithoutData(200,"Deleted successfully")
    return result
