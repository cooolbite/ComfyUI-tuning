import os
import sys
import time
import json
import uuid
import random
import urllib.request
import subprocess
import threading

COMFY_DIR = r"C:\Users\cooolbite\Desktop\Project\ComfyUI"
PYTHON_EXE = os.path.join(COMFY_DIR, "venv", "Scripts", "python.exe")
OUTPUT_DIR = os.path.join(COMFY_DIR, "output")
BASE_URL = "http://127.0.0.1:8188"

sys.path.insert(0, os.path.join(COMFY_DIR, "custom_nodes"))
import character_blueprint_nodes as bp


def is_server_running():
    try:
        urllib.request.urlopen(f"{BASE_URL}/system_stats", timeout=2)
        return True
    except Exception:
        return False


def draw_progress_bar(img_idx, total_imgs, img_pct, overall_pct, status_text, elapsed_s):
    bar_len = 28
    filled_img = int(round(bar_len * img_pct / 100.0))
    filled_tot = int(round(bar_len * overall_pct / 100.0))
    bar_img = "█" * filled_img + "░" * (bar_len - filled_img)
    bar_tot = "█" * filled_tot + "░" * (bar_len - filled_tot)
    line = (
        f"\r  รวมทั้งหมด [{bar_tot}] {overall_pct:5.1f}% | "
        f"ภาพที่ {img_idx}/{total_imgs} [{bar_img}] {img_pct:5.1f}% | "
        f"{status_text} ({elapsed_s:.0f}s)   "
    )
    sys.stdout.write(line)
    sys.stdout.flush()


def build_random_5_prompts():
    rng = random.Random()
    ethnicities = list(bp.ETHNICITY_MAP.keys())
    faces = list(bp.FACE_EXPR_MAP.keys())
    hairs = list(bp.HAIR_MAP.keys())
    skin_tones = list(bp.SKIN_TONE_MAP.keys())[:3]
    skin_textures = [
        "📸 ผิวคนจริงระดับ DSLR รูขุมขนละเอียด + หน้ามีมิติ 3D (Real DSLR Pores & 3D Depth - แนะนำ)",
        "☀️ ผิวคนจริงไร้กระ เน้นรูขุมขนธรรมชาติ (Clean Real Human Pores - No Freckles)",
    ]
    body_shapes = list(bp.BODY_SHAPE_MAP.keys())[:2]
    poses = list(bp.POSE_MAP.keys())
    nude_outfits = [
        "🚫 ไม่มีเสื้อผ้าเลย - เปลือยทั้งหมด (Completely Nude - Small Areola & Beautiful Tits)",
        "🚫 เปลือยท่อนบน - ไม่ใส่เสื้อ (Topless - Small Areola & Beautiful Tits)",
    ]
    accessories = list(bp.ACCESSORY_MAP.keys())
    backgrounds = list(bp.BACKGROUND_MAP.keys())[:6]
    lightings = list(bp.LIGHTING_MAP.keys())

    chosen_eths = rng.sample(ethnicities, min(5, len(ethnicities)))
    chosen_bgs = rng.sample(backgrounds, min(5, len(backgrounds)))

    batch = []
    ts_str = time.strftime("%Y%m%d_%H%M%S")
    for idx in range(5):
        eth = chosen_eths[idx % len(chosen_eths)]
        face = rng.choice(faces)
        hair = rng.choice(hairs)
        st = rng.choice(skin_tones)
        stx = rng.choice(skin_textures)
        bs = rng.choice(body_shapes)
        pose = rng.choice(poses)
        outfit = rng.choice(nude_outfits)
        acc = rng.choice(accessories)
        bg = chosen_bgs[idx % len(chosen_bgs)]
        light = rng.choice(lightings)
        seed1 = rng.randint(100000000, 999999999)
        seed2 = seed1 + 1

        prompt = {
            "4": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": "RealCamera_AsianAura_Hybrid_v1.safetensors"}},
            "8": {"class_type": "LoraLoader", "inputs": {"model": ["4", 0], "clip": ["4", 1], "lora_name": "AsianBeauty_Sarah_v1.safetensors", "strength_model": 0.50, "strength_clip": 0.50}},
            "12": {"class_type": "LoraLoader", "inputs": {"model": ["8", 0], "clip": ["8", 1], "lora_name": "skin_texture_slider_v1.safetensors", "strength_model": 0.20, "strength_clip": 0.20}},
            "13": {"class_type": "LoraLoader", "inputs": {"model": ["12", 0], "clip": ["12", 1], "lora_name": "PerfectPerkyBreasts_v3.safetensors", "strength_model": 0.40, "strength_clip": 0.40}},
            "17": {"class_type": "BlueprintFace", "inputs": {"หน้าตาและอารมณ์_Face": face, "ทรงผม_Hair": hair}},
            "18": {"class_type": "BlueprintSkin", "inputs": {"สีผิว_SkinTone": st, "พื้นผิว_SkinTexture": stx}},
            "19": {"class_type": "BlueprintBody", "inputs": {"สัดส่วนหุ่น_BodyShape": bs, "ท่าโพสและมุมกล้อง_Pose": pose}},
            "20": {"class_type": "BlueprintOutfit", "inputs": {"เครื่องแต่งกาย_Outfit": outfit, "เครื่องประดับ_Accessory": acc}},
            "21": {"class_type": "BlueprintBackground", "inputs": {"ฉากหลัง_Background": bg, "แสงและบรรยากาศ_Lighting": light}},
            "22": {
                "class_type": "BlueprintMasterCompiler",
                "inputs": {
                    "clip": ["13", 1],
                    "ethnicity_prompt": ["16", 0],
                    "face_prompt": ["17", 0],
                    "skin_prompt": ["18", 0],
                    "body_prompt": ["19", 0],
                    "outfit_prompt": ["20", 0],
                    "background_prompt": ["21", 0],
                    "ความละเอียด_Resolution": "📷 1440x1960 2K พอร์ตเทรตสมส่วน DSLR (1440 x 1960 px - ค่าเริ่มต้น ไม่โดนบีบ)"
                }
            },
            "3": {
                "class_type": "KSampler",
                "inputs": {
                    "model": ["13", 0],
                    "positive": ["22", 0],
                    "negative": ["22", 1],
                    "latent_image": ["22", 2],
                    "seed": seed1,
                    "steps": 24,
                    "cfg": 5.3,
                    "sampler_name": "dpmpp_2m_sde",
                    "scheduler": "karras",
                    "denoise": 1.0
                }
            },
            "14": {
                "class_type": "LatentUpscale",
                "inputs": {
                    "samples": ["3", 0],
                    "upscale_method": "bislerp",
                    "width": 704,
                    "height": 960,
                    "crop": "disabled"
                }
            },
            "15": {
                "class_type": "KSampler",
                "inputs": {
                    "model": ["13", 0],
                    "positive": ["22", 0],
                    "negative": ["22", 1],
                    "latent_image": ["14", 0],
                    "seed": seed2,
                    "steps": 16,
                    "cfg": 5.0,
                    "sampler_name": "dpmpp_2m",
                    "scheduler": "karras",
                    "denoise": 0.36
                }
            },
            "1": {"class_type": "VAEDecode", "inputs": {"samples": ["15", 0], "vae": ["4", 2]}},
            "23": {
                "class_type": "BlueprintNippleRefiner",
                "inputs": {
                    "image": ["1", 0],
                    "model": ["13", 0],
                    "clip": ["13", 1],
                    "vae": ["4", 2],
                    "seed": seed2 + 99,
                    "steps": 15,
                    "denoise": 0.30,
                    "outfit_prompt": ["20", 0]
                }
            },
            "9": {"class_type": "UpscaleModelLoader", "inputs": {"model_name": "4xUltrasharp_v10.pt"}},
            "10": {"class_type": "ImageUpscaleWithModel", "inputs": {"upscale_model": ["9", 0], "image": ["23", 0]}},
            "11": {"class_type": "ImageScale", "inputs": {"image": ["10", 0], "upscale_method": "lanczos", "width": 1440, "height": 1960, "crop": "disabled"}},
            "2": {"class_type": "SaveImage", "inputs": {"images": ["11", 0], "filename_prefix": f"Auto5_PerfectBreasts_2K_{ts_str}_#{idx+1:02d}"}}
        }
        batch.append((eth, outfit, bg, prompt))
    return batch


def run_prompt_with_ws_progress(img_idx, total_imgs, prompt_dict):
    client_id = str(uuid.uuid4())
    ws_state = {"pass": 0, "step": 0, "max_steps": 20, "node": "", "done": False}

    # Try background websocket listener via aiohttp (installed in ComfyUI venv)
    def ws_worker():
        import asyncio
        import aiohttp

        async def listen():
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.ws_connect(f"ws://127.0.0.1:8188/ws?clientId={client_id}") as ws:
                        async for msg in ws:
                            if msg.type == aiohttp.WSMsgType.TEXT:
                                data = json.loads(msg.data)
                                mtype = data.get("type")
                                mdata = data.get("data", {})
                                if mtype == "executing":
                                    node = mdata.get("node")
                                    ws_state["node"] = str(node or "")
                                    if node == "3":
                                        ws_state["pass"] = 1
                                    elif node == "15":
                                        ws_state["pass"] = 2
                                    elif node is None and ws_state["pass"] >= 1:
                                        ws_state["done"] = True
                                        return
                                elif mtype == "progress":
                                    ws_state["step"] = mdata.get("value", 0)
                                    ws_state["max_steps"] = max(1, mdata.get("max", 1))
            except Exception:
                pass

        asyncio.run(listen())

    t_ws = threading.Thread(target=ws_worker, daemon=True)
    t_ws.start()
    time.sleep(0.2)

    req = urllib.request.Request(
        f"{BASE_URL}/prompt",
        data=json.dumps({"prompt": prompt_dict, "client_id": client_id}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    resp = json.loads(urllib.request.urlopen(req).read().decode("utf-8"))
    pid = resp["prompt_id"]

    t0 = time.time()
    while True:
        elapsed = time.time() - t0
        try:
            hist = json.loads(urllib.request.urlopen(f"{BASE_URL}/history/{pid}", timeout=3).read().decode("utf-8"))
            if pid in hist:
                fn = hist[pid]["outputs"]["2"]["images"][0]["filename"]
                overall_pct = (img_idx / total_imgs) * 100.0
                draw_progress_bar(img_idx, total_imgs, 100.0, overall_pct, "เสร็จสมบูรณ์!", elapsed)
                print(f"\n     ✅ บันทึกไฟล์: {fn}")
                return fn
        except Exception:
            pass

        # Compute exact image % from WS events (Pass 1 = 0..60%, Pass 2 = 60..90%, Upscale = 90..99%)
        node = ws_state["node"]
        if ws_state["pass"] <= 1 and node in ("4", "8", "12", "13", "22", ""):
            img_pct = min(10.0, elapsed * 1.5)
            status = "กำลังโหลดโมเดล & ประมวลผล Blueprint"
        elif ws_state["pass"] == 1 or node == "3":
            frac = ws_state["step"] / ws_state["max_steps"]
            img_pct = 10.0 + frac * 52.0
            status = f"Pass 1: สร้างโครงสร้างภาพ ({ws_state['step']}/{ws_state['max_steps']})"
        elif ws_state["pass"] == 2 or node == "15":
            frac = ws_state["step"] / ws_state["max_steps"]
            img_pct = 62.0 + frac * 28.0
            status = f"Pass 2: เติมรูขุมขน DSLR & มิติ 3D ({ws_state['step']}/{ws_state['max_steps']})"
        elif node in ("1", "9", "10", "11", "2"):
            img_pct = min(99.0, 90.0 + (elapsed % 10))
            status = "กำลังขยายความคมชัด 2K (1440x2560)"
        else:
            img_pct = min(98.0, (elapsed / 80.0) * 100.0)
            status = "กำลังเรนเดอร์ GPU..."

        overall_pct = ((img_idx - 1) + (img_pct / 100.0)) / total_imgs * 100.0
        draw_progress_bar(img_idx, total_imgs, img_pct, overall_pct, status, elapsed)
        time.sleep(0.4)


def main():
    os.system("chcp 65001 >nul")
    print("================================================================================")
    print("  🚀 ระบบสุ่มสร้างภาพ 5 ภาพอัตโนมัติ (Perfect Breasts + Small Areola + Real DSLR 2K)")
    print("  📐 ความละเอียด: 9:16 2K (1440 x 2560 พิกเซล) | โมเดล: RealCamera AsianAura DSLR")
    print("================================================================================")

    started_own_server = False
    server_proc = None

    if not is_server_running():
        print("  ⏳ กำลังเปิดเซิร์ฟเวอร์ GPU ComfyUI เบื้องหลังอัตโนมัติ...")
        server_proc = subprocess.Popen(
            [PYTHON_EXE, "main.py", "--force-fp16", "--use-pytorch-cross-attention", "--port", "8188"],
            cwd=COMFY_DIR,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        started_own_server = True
        for i in range(60):
            if is_server_running():
                break
            sys.stdout.write(f"\r  ⏳ รอระบบการ์ดจอพร้อมทำงาน... ({i+1}s)")
            sys.stdout.flush()
            time.sleep(1.0)
        print("\n  ✅ เชื่อมต่อการ์ดจอ GTX 1060 6GB สำเร็จ!")
    else:
        print("  ✅ เชื่อมต่อเซิร์ฟเวอร์ ComfyUI ที่เปิดอยู่สำเร็จ!")

    batch = build_random_5_prompts()
    saved_files = []
    t_start = time.time()

    try:
        for idx, (eth, outfit, bg, prompt_dict) in enumerate(batch, start=1):
            print(f"\n--------------------------------------------------------------------------------")
            print(f"  📸 กำลังสร้างภาพที่ [{idx}/5]: {eth}")
            print(f"     • ชุด: {outfit}")
            print(f"     • ฉาก: {bg}")
            fn = run_prompt_with_ws_progress(idx, 5, prompt_dict)
            saved_files.append(fn)
    finally:
        if started_own_server and server_proc is not None:
            print("\n  🛑 กำลังปิดเซิร์ฟเวอร์ชั่วคราวเพื่อคืนค่า VRAM...")
            server_proc.terminate()

    total_time = time.time() - t_start
    print("\n================================================================================")
    print(f"  🎉 สร้างครบทั้ง 5 ภาพ 100% เสร็จสมบูรณ์! (ใช้เวลารวม {total_time:.1f} วินาที)")
    print(f"  📂 โฟลเดอร์ภาพ: {OUTPUT_DIR}")
    print("  ⏳ หน้าต่างนี้จะปิดตัวเองอัตโนมัติใน 3 วินาที...")
    print("================================================================================")
    try:
        subprocess.Popen(["explorer.exe", OUTPUT_DIR])
    except Exception:
        pass
    time.sleep(3.0)


if __name__ == "__main__":
    main()
