from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': "Hello World"} 

@app.get('/items/{item_id}')
async def item_w_id(item_id):
    return {'item_id': item_id}