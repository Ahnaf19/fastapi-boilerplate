from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from loguru import logger

from app.routes.route import router
from app.utils import fake_answer_to_everything_ml_model

ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Lifespan context manager for the FastAPI application.
    Initializes and cleans up resources.
    Can use alternative methods like `startup` and `shutdown` events.
    [deprecated but needed in lower versions]
    For more: https://fastapi.tiangolo.com/advanced/events/
    """

    # * before yield: code to run before the app starts
    # Initialize resources, connect databases, load models, etc.
    ml_models["fake_answer_to_everything"] = fake_answer_to_everything_ml_model
    logger.info("before app startup initialization")

    yield

    # * after yield: code to run after the app stops
    # Cleanup resources if needed
    # For example, close database connections or release resources
    ml_models.clear()
    logger.info("after app shutdown cleanup")


# Create an instance of the FastAPI application
app = FastAPI(lifespan=lifespan)

# Include routers for guest and room endpoints
app.include_router(router)


def main() -> None:
    """
    Entry point for the application when run explicitly.
    """
    print("main.py running explicitly")


if __name__ == "__main__":
    main()
