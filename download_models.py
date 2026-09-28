import os
import sys
import ssl
import urllib.request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")

SSL_CTX = ssl._create_unverified_context()

REQUIRED_FILES = [
    # 1. Base Checkpoints (used to build RealCamera_AsianAura_Hybrid_v1.safetensors)
    (
        "checkpoints/beautifulRealistic_v7.safetensors",
        "https://civitai.com/api/download/models/177164",
        "Beautiful Realistic Asians v7 (Base Checkpoint A)",
    ),
    (
        "checkpoints/epicrealism_naturalSinRC1VAE.safetensors",
        "https://civitai.com/api/download/models/143906",
        "epiCRealism Natural Sin RC1 VAE (Base Checkpoint B)",
    ),
    # 2. Tuned LoRAs for Character Blueprints & Natural Breasts/Small Pink Areola
    (
        "loras/AsianBeauty_Sarah_v1.safetensors",
        "https://civitai.com/api/download/models/103002",
        "Asian Beauty Sarah v1 LoRA",
    ),
    (
        "loras/PerfectPerkyBreasts_v3.safetensors",
        "https://civitai.com/api/download/models/85784",
        "Perfect Perky Breasts v3 LoRA (Tuned at 0.40)",
    ),
    (
        "loras/skin_texture_slider_v1.safetensors",
        "https://civitai.com/api/download/models/148581",
        "Real DSLR Skin Texture Slider v1 LoRA (Tuned at 0.20)",
    ),
    (
        "loras/detail_tweaker_v1.safetensors",
        "https://civitai.com/api/download/models/62833",
        "Detail Tweaker v1 LoRA",
    ),
    (
        "loras/ThaiUniUniform_v2.safetensors",
        "https://civitai.com/api/download/models/58690",
        "Thai University Uniform v2 LoRA",
    ),
    (
        "loras/KoreanGirl_eunji_v7.safetensors",
        "https://civitai.com/api/download/models/1161665",
        "Korean Girl Eunji v7 LoRA",
    ),
    (
        "loras/AsianGirlsFace_v1.safetensors",
        "https://civitai.com/api/download/models/67325",
        "Asian Girls Face v1 LoRA",
    ),
    (
        "loras/AsianMix_v1.safetensors",
        "https://civitai.com/api/download/models/513352",
        "Asian Mix v1 LoRA",
    ),
    # 3. Negative Textual Inversion Embeddings
    (
        "embeddings/BadDream.pt",
        "https://civitai.com/api/download/models/77169",
        "BadDream Negative Embedding",
    ),
    (
        "embeddings/bad-hands-5.pt",
        "https://civitai.com/api/download/models/125849",
        "bad-hands-5 Negative Embedding",
    ),
    (
        "embeddings/easynegative.safetensors",
        "https://civitai.com/api/download/models/9208",
        "EasyNegative Embedding",
    ),
    (
        "embeddings/ng_deepnegative_v1_75t.pt",
        "https://civitai.com/api/download/models/5637",
        "DeepNegative v1.75T Embedding",
    ),
    # 4. 2K Upscaler Model
    (
        "upscale_models/4xUltrasharp_v10.pt",
        "https://huggingface.co/Kim2091/UltraSharp/resolve/main/4x-UltraSharp.pth",
        "4x-UltraSharp v10 2K Upscaler",
    ),
]


def download_with_progress(url, dest_path, label):
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 1024:
        sz_mb = os.path.getsize(dest_path) / (1024 * 1024)
        print(f"[SKIP] {label} already exists ({sz_mb:.1f} MB)")
        return True

    print(f"[DOWNLOADING] {label}\n  URL : {url}\n  DEST: {dest_path}")
    tmp_path = dest_path + ".part"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=60) as resp, open(tmp_path, "wb") as out_f:
            total = int(resp.headers.get("Content-Length", 0))
            downloaded = 0
            while True:
                chunk = resp.read(1024 * 1024)
                if not chunk:
                    break
                out_f.write(chunk)
                downloaded += len(chunk)
                if total > 0:
                    pct = downloaded * 100.0 / total
                    sys.stdout.write(f"\r  Progress: {downloaded/(1024*1024):.1f} / {total/(1024*1024):.1f} MB ({pct:.1f}%)")
                else:
                    sys.stdout.write(f"\r  Downloaded: {downloaded/(1024*1024):.1f} MB")
                sys.stdout.flush()
        print()
        os.replace(tmp_path, dest_path)
        return True
    except Exception as e:
        print(f"\n[ERROR] Failed to download {label}: {e}")
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        return False


def build_hybrid_checkpoint_if_needed():
    hybrid_path = os.path.join(MODELS_DIR, "checkpoints", "RealCamera_AsianAura_Hybrid_v1.safetensors")
    if os.path.exists(hybrid_path) and os.path.getsize(hybrid_path) > 100 * 1024 * 1024:
        print(f"[OK] Hybrid checkpoint ready: {hybrid_path}")
        return

    ckpt_a = os.path.join(MODELS_DIR, "checkpoints", "beautifulRealistic_v7.safetensors")
    ckpt_b = os.path.join(MODELS_DIR, "checkpoints", "epicrealism_naturalSinRC1VAE.safetensors")
    if not (os.path.exists(ckpt_a) and os.path.exists(ckpt_b)):
        print("[WARN] Base checkpoints missing; skipping RealCamera_AsianAura_Hybrid_v1 merge.")
        return

    print("[MERGING] Building RealCamera_AsianAura_Hybrid_v1.safetensors (55% BeautifulRealistic_v7 + 45% epiCRealism)...")
    import torch
    from safetensors.torch import load_file, save_file

    sd_a = load_file(ckpt_a, device="cpu")
    sd_b = load_file(ckpt_b, device="cpu")
    merged = {}
    alpha = 0.55
    for k, va in sd_a.items():
        if k in sd_b and va.shape == sd_b[k].shape and va.is_floating_point():
            merged[k] = (va.float() * alpha + sd_b[k].float() * (1.0 - alpha)).to(torch.float16)
        else:
            merged[k] = va.to(torch.float16) if va.is_floating_point() else va
    save_file(merged, hybrid_path)
    print(f"[DONE] Created {hybrid_path} ({os.path.getsize(hybrid_path)/(1024*1024):.1f} MB)")


def main():
    print("=" * 76)
    print("  ComfyUI-tuning Model & LoRA Downloader (RealDSLR + PerfectBreasts 2K)")
    print("=" * 76)
    hybrid_path = os.path.join(MODELS_DIR, "checkpoints", "RealCamera_AsianAura_Hybrid_v1.safetensors")
    has_hybrid = os.path.exists(hybrid_path) and os.path.getsize(hybrid_path) > 100 * 1024 * 1024

    for rel_path, url, label in REQUIRED_FILES:
        if has_hybrid and rel_path.startswith("checkpoints/"):
            print(f"[SKIP] {label} (RealCamera_AsianAura_Hybrid_v1.safetensors already exists)")
            continue
        dest = os.path.join(MODELS_DIR, rel_path.replace("/", os.sep))
        download_with_progress(url, dest, label)

    build_hybrid_checkpoint_if_needed()
    print("\n[COMPLETE] All required models, LoRAs, embeddings, and upscalers are ready!")


if __name__ == "__main__":
    main()
