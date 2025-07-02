import os
from datetime import datetime
import cv2
import torch
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

model = None

def load_model():
    global model
    if model is None:
        print("🔧 Loading Real-ESRGAN for deblurring...")
        model_path = "models/deblur/RealESRGAN_x4plus.pth"
        model = RealESRGANer(
            scale=4,
            model_path=model_path,
            model=RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64,
                          num_block=23, num_grow_ch=32, scale=4),
            tile=0,
            tile_pad=10,
            pre_pad=0,
            half=torch.cuda.is_available()
        )
    return model

def deblur_image(input_image_path: str) -> str:
    model = load_model()
    print(f"🔧 Deblurring: {input_image_path}")
    img = cv2.imread(input_image_path, cv2.IMREAD_COLOR)

    if img is None:
        return "❌ Invalid image path or format."

    output, _ = model.enhance(img, outscale=4)

    out_dir = "output/deblurred"
    os.makedirs(out_dir, exist_ok=True)
    filename = f"deblur_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    output_path = os.path.join(out_dir, filename)
    cv2.imwrite(output_path, output)
    print(f"✅ Deblurred image saved: {output_path}")
    return output_path
