import clip
import torch

from io import BytesIO
from PIL import Image

CLIP_MODEL = "ViT-L/14@336px"

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load(CLIP_MODEL, device=device)


class Embedder:
    @staticmethod
    def load_and_preprocess_image(image: bytes):
        img = Image.open(BytesIO(image))

        # resize image to 800x(WIDTH)
        WIDTH = 800
        wpercent = 800 / float(img.size[0])
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((WIDTH, hsize), Image.ANTIALIAS)

        img_preprocessed = preprocess(img)
        img_preprocessed = img_preprocessed.unsqueeze(0).to(device)  # type: ignore

        return img_preprocessed

    @staticmethod
    def image_embeddings(image: bytes):
        preprocessed_image = Embedder.load_and_preprocess_image(image)

        with torch.no_grad():
            embeddings = model.encode_image(preprocessed_image)

        embeddings = embeddings.cpu().numpy().flatten()
        return list(embeddings)
