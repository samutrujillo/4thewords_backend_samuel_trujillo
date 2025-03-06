from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Form

from sqlmodel import Session

from app.core.database import get_session
from app.schemas.legend_schema import LegendCreate
from app.services.legend_service import create_legend, upload_image_to_s3

router = APIRouter()

@router.get("/health")
def health_check():
    return {"message": "Health Check OK"}


@router.post("/legends/")
def create_legend_endpoint(
    name: str = Form(...),
    category: str = Form(...),
    description: str = Form(...),
    date: str = Form(...),
    province: str = Form(...),
    canton: str = Form(...),
    district: str = Form(...),
    image: UploadFile = File(...),
    session: Session = Depends(get_session),
):
    try:
        image_url = upload_image_to_s3(image)

        legend_data = LegendCreate(
            name=name,
            category=category,
            description=description,
            date=date,
            province=province,
            canton=canton,
            district=district,
            image_url=image_url,
        )

        legend = create_legend(session, legend_data)
        return legend
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))