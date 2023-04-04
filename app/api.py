import traceback


from fastapi import FastAPI, UploadFile
from starlette.responses import RedirectResponse

from app.embedder import Embedder
from app.models import ImageEmbeddingsResponse


IMAGES_TYPES = ["image/png", "image/jpg", "image/jpeg", "image/webp"]

app = FastAPI()


@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"/docs", status_code=301)


@app.post("/image/embeddings", response_model=ImageEmbeddingsResponse)
async def image_embeddings(image: UploadFile):
    if image.content_type not in IMAGES_TYPES:
        return {
            "error": {
                "code": 400,
                "message": f"Image type {image.content_type} is not supported",
                "name": "INVALID_FILE_TYPE",
            }
        }

    try:
        file = await image.read()
        embeddings = Embedder.image_embeddings(file)

        return {
            "data": {
                "content_type": image.content_type,
                "embeddings": embeddings,
                "filename": image.filename,
                "size": image.size,
            }
        }

    except Exception as e:
        # print(e)
        # traceback.print_exc()
        lines = traceback.format_exception(e)
        message = "".join(lines)

        return {"error": {"code": 500, "message": message}}
