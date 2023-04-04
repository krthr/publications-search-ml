from pathlib import Path

from app.api import app
from starlette.testclient import TestClient


def test_api():
    client = TestClient(app)

    TEST_IMAGES = ["./app/data/img1.jpg", "./app/data/img2.png"]

    paths = map(lambda path: Path(path), TEST_IMAGES)

    for image in paths:
        file = image.open("rb")

        response = client.post(
            "/image/embeddings",
            files={"image": file},
        )

        assert response.status_code == 200

        record = response.json()

        assert record["error"] is None
        assert record["data"] is not None

        data = record["data"]

        assert data["content_type"] is not None
        assert data["embeddings"] is not None
        assert data["filename"] is not None
        assert data["size"] is not None

        assert data["filename"] == str(image).split("/")[-1]
        assert data["size"] == image.stat().st_size

        embeddings = data["embeddings"]
        assert type(embeddings) == list
        assert len(embeddings) == 512
