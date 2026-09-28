# ComfyUI-tuning

Tuned **RealDSLR + Perfect Breasts & Small Rose-Pink Areola (`1440 x 1960` 2K Un-stretched)** Character Blueprint pipeline for ComfyUI.

## 📦 Essential Files Included
- `download_models.py` / `download_models.bat` — Automatic downloader for all required Checkpoints, LoRAs, Negative Embeddings, and `4xUltrasharp_v10.pt` (plus automatic `RealCamera_AsianAura_Hybrid_v1.safetensors` FP16 merge)
- `custom_nodes/character_blueprint_nodes.py` — Tuned Character Blueprint nodes (`BlueprintEthnicity`, `BlueprintFace`, `BlueprintSkin`, `BlueprintBody`, `BlueprintOutfit`, `BlueprintBackground`, `BlueprintMasterCompiler`, `BlueprintNippleRefiner`)
- `generate_5_random_2k.py` / `สุ่มสร้าง_5_ภาพ_2K_Auto.bat` — One-click 5-image 2K (`1440 x 1960`) batch generator with real-time progress bar
- `user/default/workflows/blueprint_selector_2K_9x16.json` & `default_9x16_2K_1440x2560.json` — Pre-tuned ComfyUI 2K workflows (`512x704` -> `704x960` -> `1440x1960`)

## 🚀 Quick Start
1. Copy these files into your `ComfyUI` root folder.
2. Double-click **`download_models.bat`** (or run `python download_models.py`) to download all required models, LoRAs, embeddings, and upscaler automatically.
3. Double-click **`สุ่มสร้าง_5_ภาพ_2K_Auto.bat`** (or **`run_nvidia_gpu.bat`**) to generate 2K DSLR images (`1440 x 1960`).
