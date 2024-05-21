from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from api import authorcontroller, get_db
from api import AuthorSchema, AuthorCreateSchema, AuthorUpdateSchema

# Enrutador donde se definen los endpoints
router = APIRouter()


@router.get("/", response_model=list[AuthorSchema])
async def read_author(db: Session = Depends(get_db)):
    authors = authorcontroller.get_authors(db)
    if authors == None:
        raise HTTPException(status_code=503, detail="DB Unavailable")
    return authors


@router.get("/{author_id}", response_model=AuthorSchema)
async def read_author(author_id: int, db: Session = Depends(get_db)):
    author = authorcontroller.get_author(db, author_id)
    if author == None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.post("/", response_model=AuthorSchema)
async def write_author(author: AuthorCreateSchema, db: Session = Depends(get_db)):
    authorResult = authorcontroller.write_author(db, author)
    return authorResult


@router.put("/{author_id}", response_model=AuthorSchema)
async def update_author(author_id: int, author: AuthorUpdateSchema, db: Session = Depends(get_db)):
    authorResult = authorcontroller.update_author(db, author_id, author)
    if authorResult == None:
        raise HTTPException(status_code=404, detail="Author not found")
    return authorResult


@router.delete("/{author_id}", response_model=list[AuthorSchema])
async def delete_author(author_id: int, db: Session = Depends(get_db)):
    authors = authorcontroller.delete_author(db, author_id)
    if authors == None:
        raise HTTPException(status_code=404, detail="Author not found")
    return authors
