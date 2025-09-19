from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'https://my-frontend.com','https://another-allowed-origin.com'
    ],  
    allow_credentials=True,
    allow_methods=['GET','POST','PUT','DELETE'], 
    allow_headers=["*"],  # Allows all headers
)

## define end point