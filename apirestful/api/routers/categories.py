from fastapi import Depends , APIRouter
from sqlalchemy.orm import Session
from api import categorycontroller,get_db
from api import CategorySchema, CategoryCreateSchema

#Enrutador donde se definen los endpoints
router = APIRouter()
@router.get("/", response_model=list[CategorySchema])
async def read_categories(db: Session = Depends(get_db)):
    categories=categorycontroller.get_categories(db)
    return categories

@router.get("/{cat_id}", response_model=CategorySchema)
async def read_category(cat_id:int,db: Session = Depends(get_db)):
    category=categorycontroller.get_category(db,cat_id)
    return category

@router.post("/", response_model=CategorySchema)
async def write_category(category:CategoryCreateSchema,db: Session = Depends(get_db)):
    categoryResult=categorycontroller.write_category(db,category)
    return categoryResult

@router.put("/{cat_id}", response_model=CategorySchema)
async def update_category(cat_id:int,category:CategoryCreateSchema,db: Session = Depends(get_db)):
    categoryResult = categorycontroller.update_category(db, cat_id,category)
    return categoryResult

@router.delete("/{cat_id}", response_model=list[CategorySchema])
async def delete_category(cat_id:int, db: Session = Depends(get_db)):
    return categorycontroller.delete_category(db, cat_id)
