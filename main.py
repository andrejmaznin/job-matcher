from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def hello(name: str = "World"):
    """
    Greet a user by name

    - **name**: Name to greet (query parameter, defaults to 'World')
    """
    return {"message": f"Hello, {name}!"}