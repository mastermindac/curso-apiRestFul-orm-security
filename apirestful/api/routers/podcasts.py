from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from api import podcastcontroller, get_db
from api import PodcastSchema, PodcastCreateSchema, PodcastUpdateSchema, PodcastAuthorsSchema, PodcastAuthorCreateSchema

# Enrutador donde se definen los endpoints
router = APIRouter()


@router.get("/", response_model=list[PodcastSchema])
async def read_podcast(db: Session = Depends(get_db)):
    podcasts = podcastcontroller.get_podcasts(db)
    if podcasts == None:
        raise HTTPException(status_code=503, detail="DB Unavailable")
    return podcasts


@router.get("/{podcast_id}", response_model=PodcastSchema)
async def read_podcast(podcast_id: int, db: Session = Depends(get_db)):
    podcast = podcastcontroller.get_podcast(db, podcast_id)
    if podcast == None:
        raise HTTPException(status_code=404, detail="Podcast not found")
    return podcast


@router.get("/{podcast_id}/authors", response_model=PodcastAuthorsSchema)
async def read_podcast_authors(podcast_id: int, db: Session = Depends(get_db)):
    podcast = podcastcontroller.get_podcast(db, podcast_id)
    if podcast == None:
        raise HTTPException(status_code=404, detail="Podcast not found")
    return podcast


@router.post("/", response_model=PodcastAuthorsSchema)
async def write_podcast(podcast: PodcastCreateSchema, db: Session = Depends(get_db)):
    podcastResult = podcastcontroller.write_podcast(db, podcast)
    return podcastResult


@router.post("/{podcast_id}/authors", response_model=PodcastAuthorsSchema)
async def write_podcastauthors(podcast_id: int, podcast: PodcastAuthorCreateSchema, db: Session = Depends(get_db)):
    podcastResult = podcastcontroller.write_podcastauthors(db, podcast_id, podcast)
    if podcastResult == None:
        raise HTTPException(status_code=404, detail="Duplicated author-podcast")
    return podcastResult


@router.put("/{podcast_id}", response_model=PodcastSchema)
async def update_podcast(podcast_id: int, podcast: PodcastUpdateSchema, db: Session = Depends(get_db)):
    podcastResult = podcastcontroller.update_podcast(db, podcast_id, podcast)
    if podcastResult == None:
        raise HTTPException(status_code=406, detail="Podcast not found")
    return podcastResult


@router.delete("/{podcast_id}", response_model=list[PodcastSchema])
async def delete_podcast(podcast_id: int, db: Session = Depends(get_db)):
    podcasts = podcastcontroller.delete_podcast(db, podcast_id)
    if podcasts == None:
        raise HTTPException(status_code=404, detail="Podcast not found")
    return podcasts


@router.delete("/{podcast_id}/authors", response_model=PodcastAuthorsSchema)
async def delete_podcast(podcast_id: int, podcast: PodcastAuthorCreateSchema, db: Session = Depends(get_db)):
    podcasts = podcastcontroller.delete_podcastauthors(db, podcast_id, podcast)
    if podcasts == None:
        raise HTTPException(status_code=404, detail="Podcast not found")
    return podcasts
