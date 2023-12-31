import strawberry
from typing import Union
from fastapi import FastAPI
from strawberry.asgi import GraphQL

@strawberry.type
class User:
  name: str
  age: int

@strawberry.type
class Query:
  @strawberry.field
  def user(self) -> User:
    return User(name="Proud", age=26)
  
schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}