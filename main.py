from fastapi import FastAPI

app = FastAPI()

@app.post("/numbers/")
async def post2Nums(num1:int, num2:int):
    return num1 + num2

@app.get("/numbers/")
async def sumOf2Nums(num1:int, num2:int):
    return {"zbir broja " + str(num1) + " i broja " + str(num2) + " je:": num1 + num2}