from fastapi import APIRouter
from api import categorycontroller

#Enrutador donde se definen los endpoints
router = APIRouter()
@router.get("/")
async def read_categories():
    return categorycontroller.get_categories()

@router.post("/")
async def write_category():
    return {"msg":"POST CATEGORY"}

@router.put("/")
async def update_category():
    return {"msg":"PUT CATEGORY"}

@router.delete("/")
async def delete_category():
    return {"msg":"DELETE CATEGORY"}
