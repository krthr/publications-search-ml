import clip
import torch


CLIP_MODEL = "ViT-L/14@336px"

print(f"using model={CLIP_MODEL}")

device = "cuda" if torch.cuda.is_available() else "cpu"
clip.load(CLIP_MODEL, device=device)

print('download completed')