from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int

users_list = [
    User(id=1, name="Emmanuel", age=30),
    User(id=2, name="John", age=25)
]

# GET

@app.get("/users")
async def users():
    return users_list

# Path
@app.get("/user/{id}")
async def user_by_id(id: int):
    return find_user(id)

# Query    
@app.get("/user/")
async def user_by_query(id: int):
    return find_user(id)

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Emmanuel", "age": 30}, 
            {"name": "John", "age": 25}]

# POST

@app.post("/user/", status_code=201)
async def create_user(user: User):
    searched_user = find_user(user.id)
    if type(searched_user) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user

# PUT

@app.put("/user/")
async def update_user(user: User, status_code=201):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# DELETE

@app.delete("/user/{id}")
async def delete_user(id: int):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            return {"message": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

def find_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")