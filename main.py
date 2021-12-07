from fastapi import FastAPI

from View import task_view, user_view

app = FastAPI()


app.include_router(task_view.router)
app.include_router(user_view.router)


@app.get("/")
async def root():
    return {"message": "This is Task Applications!"}
