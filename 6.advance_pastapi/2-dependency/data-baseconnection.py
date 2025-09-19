from fastapi import FastAPI,Depends
app=FastAPI()

## dependancy func
def get_db():
    db={'connection':'mock_db_connection'}
    try:
        
        yield db ## yeild is use to return the value and also to pause the function execution
    finally:
        db.close()






## endpoint
@app.get("/home")
def home(db=Depends(get_db)):
    return {'db_status':db['connection']}
    