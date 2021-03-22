from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import ValidationError
from egob.logger import logger
from egob.model.virtuoso import Virtuoso


router = APIRouter()

@router.get("/create_id", name="See the coordinates of all locations of create_id", tags=["consultas"])
async def create_id():
    CID = None
    try:
        CID = Virtuoso.create_id()
    except ValidationError as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=f"Not found")
    except Exception as e:
        logger.exception(e)
    
    return CID