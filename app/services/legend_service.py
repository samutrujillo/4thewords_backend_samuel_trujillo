import uuid

import boto3

from app.core.config import settings
from app.models.legend_model import Legend
from sqlmodel import Session
from app.schemas.legend_schema import LegendCreate


def create_legend(session: Session, legend_data: LegendCreate):
    legend = Legend(**legend_data.dict())
    session.add(legend)
    session.commit()
    session.refresh(legend)
    return legend


def upload_image_to_s3(image_file):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION,
    )

    file_extension = image_file.filename.split(".")[-1]
    file_name = f"legends/{uuid.uuid4()}.{file_extension}"

    s3.upload_fileobj(
        image_file.file,
        settings.AWS_BUCKET_NAME,
        file_name,
        ExtraArgs={"ContentType": image_file.content_type}
    )

    return f"https://{settings.AWS_BUCKET_NAME}.s3.{settings.AWS_REGION}.amazonaws.com/{file_name}"
