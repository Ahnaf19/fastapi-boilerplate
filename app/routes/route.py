from fastapi import APIRouter

from app.pydantic_models.pydantic_model import ResponseModel
from app.services.service import Service

# Initialize the router with a prefix and tags
router = APIRouter(prefix="/group", tags=["group"])

# Initiate the Service
service = Service()


# Define the routes
@router.get("/", response_model=ResponseModel)
async def read_data() -> ResponseModel:
    """
    Retrieve all data.

    Returns:
        ResponseModel: A list of all data.
    """
    response = {"message": "ok"}
    return ResponseModel(**response)
