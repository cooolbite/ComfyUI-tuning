import torch

ETHNICITY_MAP = {
    "🇰🇷 สาวเกาหลี K-Pop / นางเอกเกาหลี (Korean Ulzzang & Actress)": "gorgeous young South Korean k-pop idol and actress, ulzzang, Korean beauty, fair milky-white rosy skin, delicate V-line face, high slim sculpted 3D nose bridge, natural Korean double eyelids, soft puffy aegyo-sal under eyes, glossy rose-pink lips",
    "🇨🇳 สาวจีนขาวหมวย เน็ตไอดอลเตDouyin (Chinese Douyin / Xiaohongshu Beauty)": "stunning young Chinese woman, Chinese beauty, fair porcelain-white luminous skin, delicate refined Chinese facial features, slim high 3D nose bridge, expressive almond eyes, soft peach-pink makeup, sculpted cheekbones",
    "🇹🇭 สาวไทยขาวหมวย / เน็ตไอดอลกรุงเทพฯ (Thai-Chinese Bangkok Net Idol)": "gorgeous young Thai-Chinese net idol woman from Bangkok, fair creamy-white rosy skin, sweet modern Thai-East Asian facial features, high slim 3D nose bridge, big expressive dark brown eyes, sweet gentle smile, natural 3D facial contours",
    "🇹🇭 สาวไทยหน้าหวานคม พิมพ์นิยมดาราไทย (Classic Sweet Thai Actress)": "stunning young Thai actress, radiant fair-warm glowing skin, sweet expressive eyes with long eyelashes, high sculpted 3D nose bridge, delicate oval face, graceful Thai beauty",
    "🇯🇵 สาวญี่ปุ่น กราเวียร์ไอดอล (Japanese Gravure Idol & Model)": "gorgeous young Japanese gravure model, fair translucent dewy skin, cute refined Japanese facial features, soft expressive eyes, natural 3D nose bridge, glossy lips",
    "🇹🇭🇬🇧 ลูกครึ่งไทย-ยุโรป ดารานางแบบ (Eurasian / Luk-Khrueng Supermodel)": "stunning young Eurasian mixed Thai-European supermodel, fair luminous skin, deep-set expressive eyes, high sculpted nose bridge, 3D facial bone structure",
}

FACE_EXPR_MAP = {
    "✨ หันข้าง 3/4 มองเหม่อริมทะเล (3/4 Side Glance Away)": "torso angled 3/4 away from camera, face turned to her right looking off into the distance away from camera, gentle parted rose-pink lips, natural calm expression",
    "😊 ยิ้มหวานชำเลืองมองด้านข้าง (Sweet Smile & Playful Side Glance)": "sweet and gentle smile with a playful twist of glancing eyes to the side, natural expressive eyes, soft natural catchlights",
    "🔥 สบตากล้องแบบเย้ายวน (Seductive Direct Eye Contact)": "looking directly at the camera with a sultry seductive gaze, slightly parted glossy lips, intense realistic eye catchlights, confident expression",
    "👑 สวยหรูดูแพง หน้านิ่งนางแบบเกาหลี (High-Fashion Korean Model Look)": "confident luxury Korean magazine model expression, relaxed sensual lips, sculpted V-line jawline, deep expressive eyes",
    "🌸 ไร้เดียงสา ตากลมโตฉ่ำหวาน (Innocent Doe-Eyed Sweet Look)": "innocent gentle expression, big expressive doe eyes, delicate natural features, subtle sweet smile",
}

HAIR_MAP = {
    "🌬️ ผมยาวดัดลอนเกาหลีสีน้ำตาลเข้มปลิวตามลม (Korean Wavy Brown Windblown)": "long Korean wavy dark brown hair flowing dynamically lifted by breeze, wispy see-through air bangs, individual flyaway hair strands",
    "🌺 เกล้ามวยสูงประดับพวงมาลัยมะลิ (Thai Jasmine Garland High Bun)": "elegant braided high bun hairstyle adorned with a traditional Thai jasmine garland with pink rose buds draping down the side",
    "💧 ผมยาวดำขลับเปียกน้ำแนบผิว (Wet Glossy Black Hair)": "long dark black wet hair clinging softly to neck and shoulders, realistic wet hair strands",
    "🖤 ผมยาวตรงสลวยสีดำธรรมชาติทรงไอดอล (Long Silky Straight Idol Black Hair)": "long silky straight jet-black hair with Korean side-parted bangs, natural shine and fine individual strands",
    "👱‍♀️ ผมยาวลอนใหญ่สีน้ำตาลคาราเมล (Caramel Brown Luxury Waves)": "long voluminous caramel-brown wavy hair with golden sunlit highlights",
    "💇‍♀️ ผมสั้นประบ่าสไตล์เกาหลี (Korean Chic Shoulder-Length Bob)": "stylish Korean shoulder-length dark brown bob hair with soft see-through bangs framing the face",
}

SKIN_TONE_MAP = {
    "🥛 ผิวขาวอมชมพู มีออร่าธรรมชาติ (Fair Milky-White Glowing Aura Skin)": "fair milky-white real human skin with radiant natural aura, soft natural blush, realistic subsurface scattering",
    "🌸 ผิวขาวเหลืองเนียนใส สไตล์สาวไทยขาวหมวย (Fair-Ivory Thai-Chinese Glowing Skin)": "creamy fair-ivory luminous real human skin, radiant complexion, natural soft shadow transitions",
    "✨ ผิวขาวฉ่ำโกลว์สุขภาพดี สไตล์เกาหลี (Radiant Korean Dewy Skin)": "dewy luminous real human skin with fine natural pores, hydrated sheen, soft natural undertones",
    "🍯 ผิวสีน้ำผึ้งโกลว์แดดธรรมชาติ (Warm Sun-Kissed Honey Skin)": "warm sun-kissed golden honey real human skin, radiant sunlit highlights, natural glowing complexion",
}

SKIN_TEXTURE_MAP = {
    "📸 ผิวคนจริงระดับ DSLR รูขุมขนละเอียด + หน้ามีมิติ 3D (Real DSLR Pores & 3D Depth - แนะนำ)": "natural human skin texture, natural 3D facial bone structure, defined nose bridge shadows, zero beauty filter, unretouched DSLR skin",
    "💦 ผิวฉ่ำน้ำโกลว์ธรรมชาติ (Dewy Glowing Skin)": "dewy glowing real human skin, hydrated soft sheen, natural specular highlights",
    "☀️ ผิวคนจริงเนียนใสธรรมชาติ (Clean Real Human Skin - No Freckles)": "real human skin texture, realistic optical skin sheen, no freckles, no blemishes, no spots",
}

BODY_SHAPE_MAP = {
    "⏳ หุ่นนาฬิกาทราย เอวคอด อกสวยสมมาตร (Curvy Hourglass & Beautiful Breasts)": "slender curvy hourglass figure, narrow waist, natural medium perky symmetrical breasts, small light pink areola, small pink nipples, toned feminine proportions",
    "🔥 หุ่นนางแบบกราเวียร์ เอวเอส อกอิ่มสวย (Voluptuous Busty Gravure Figure)": "voluptuous hourglass figure, natural full perky symmetrical breasts, small light pink areola, small pink nipples, slim cinched waist, feminine silhouette",
    "🦢 หุ่นเพรียวบาง ขายาว สไตล์ไอดอลเกาหลี (Slender K-Pop Idol Figure)": "slender graceful K-Pop idol figure, delicate collarbones, natural medium perky breasts, small light pink areola, small pink nipples, slim toned waist",
    "💪 หุ่นฟิตเฟิร์ม สุขภาพดี (Toned Athletic Fit Curvy)": "toned athletic curvy body, firm flat stomach, natural firm perky breasts, small light pink areola, small pink nipples, healthy radiant physique",
}

POSE_MAP = {
    "🛥️ โน้มตัวไปข้างหน้าเล็กน้อย มุมพอร์ตเทรตครึ่งตัว (Medium Close-Up Portrait)": "photorealistic medium close-up portrait from head to waist, centered in frame, both arms resting straight down at her sides, hands out of frame, no hands visible, clean single arm silhouette",
    "📸 พอร์ตเทรตครึ่งตัว อกสวยสมมาตร (Waist-Up Symmetrical Portrait)": "photorealistic close-up portrait from head to waist, standing straight, both arms resting straight down at her sides, hands out of frame, no hands visible, clean shoulder and arm line",
    "💃 ยืนโพสท่า S-Curve โชว์สัดส่วน (Standing Sensual S-Curve Pose)": "medium waist-up portrait, standing in a gentle S-curve posture, both arms relaxed straight down at her sides, hands out of frame, accentuating waist and chest",
    "🛏️ เอนตัวพิงหมอน/เตียงหรู (Reclining Waist-Up Portrait)": "medium close-up portrait from head to waist reclining softly against white pillows, both arms resting straight down at her sides, hands out of frame, relaxed natural posture",
    "🔙 หันข้าง 3/4 โชว์สัดส่วน (3/4 Side-Angled Waist-Up Portrait)": "medium close-up portrait from head to waist at a 3/4 angle, both arms resting straight down at her sides, hands out of frame, clean shoulder line and side profile",
}

OUTFIT_MAP = {
    "🚫 ไม่มีเสื้อผ้าเลย - เปลือยทั้งหมด (Completely Nude - Small Areola & Beautiful Tits)": "completely nude, unclothed, bare breasts, natural well-proportioned perky breasts, small light pink areola, small neat pink nipples, natural anatomical body",
    "🚫 เปลือยท่อนบน - ไม่ใส่เสื้อ (Topless - Small Areola & Beautiful Tits)": "topless, unclothed upper body, bare breasts, natural well-proportioned perky breasts, small light pink areola, small neat pink nipples, wearing only a sheer low-rise bottom",
    "🎓 ชุดนักศึกษาไทย เสื้อขาวรัดรูปกระโปรงทรงเอ (Thai University Uniform)": "mahalaiuniform, wearing fitted Thai university uniform, tight white short-sleeve button shirt accentuating bust, silver buttons, black slim pencil skirt",
    "👙 บิกินี่สายเดี่ยวไมโครตัวจิ๋ว (Micro String Bikini)": "wearing a tiny minimalist micro string bikini, thin straps, accentuating curves and fair skin",
    "🩱 ชุดชั้นในลูกไม้ซีทรูบางเบา (Sheer Transparent Lace Lingerie)": "wearing ultra-sheer transparent French lace lingerie, see-through delicate floral lace bralette",
    "👗 ชุดเดรสลูกไม้คอร์เซ็ตไทยโรแมนติก (Ivory-Pink Floral Lace Corset Dress)": "wearing a fitted ivory-white floral lace bodycon dress with a softly structured corset-inspired bodice, sweetheart neckline, wide delicate lace shoulder straps, blush-pink chiffon ruffles",
    "👚 เสื้อเชิ้ตขาวเปียกน้ำปลดกระดุม (Wet Unbuttoned See-Through White Shirt)": "wearing an oversized wet unbuttoned white shirt clinging to skin, deep open neckline, no bra underneath",
    "👘 เสื้อคลุมผ้าไหมหลุดไหล่ (Open Silk Robe Off-Shoulder)": "wearing a luxurious champagne silk robe slipping off both shoulders, open front revealing cleavage and fair skin",
}

ACCESSORY_MAP = {
    "💎 สร้อยคอจี้ทอง + ต่างหูมุก + กำไลทอง (Gold Necklace, Pearl Earrings & Bracelet)": "wearing dainty gold clover pendant necklace, pearl drop earrings, thin gold bracelet on wrist",
    "🌼 พวงมาลัยดอกมะลิ + ต่างหูระย้า (Thai Jasmine Garland & Drop Earrings)": "adorned with delicate traditional Thai jasmine garland and crystal drop earrings",
    "✨ สร้อยคอเพชรเส้นเล็กหรูหรา (Minimalist Diamond Pendant)": "wearing a minimalist solitaire diamond pendant necklace resting on collarbone",
    "🚫 ไม่มีเครื่องประดับ (No Jewelry / Bare Skin)": "no jewelry, bare neck and ears",
}

BACKGROUND_MAP = {
    "🛥️ ดาดฟ้าเรือยอชต์หรูกลางทะเลสีฟ้า (Luxury White Yacht & Blue Ocean)": "on the deck of a luxury white yacht, wooden railing, sparkling bright blue ocean and soft distant coastline in background, clear pale blue sky with wispy clouds",
    "🌸 ร้านดอกไม้ไทยโบราณ (Traditional Thai Flower Shop)": "in a traditional Thai flower shop with soft out-of-focus bokeh background of colorful flower buckets, white chrysanthemum, pink lotus, jasmine garlands hanging in background",
    "🏖️ ชายหาดส่วนตัวน้ำทะเลใส (Private Tropical Turquoise Beach)": "on a secluded luxury tropical white sand beach, crystal clear turquoise ocean waves, palm shadows in background",
    "🛁 ห้องน้ำหินอ่อนหรู & อ่างอาบน้ำ (Luxury Marble Bathroom & Steam)": "inside an opulent white marble bathroom, warm misty steam, freestanding soaking tub in background, soft glass reflections",
    "🛏️ ห้องนอนเพนต์เฮาส์หรูผ้าปูซาติน (Luxury Penthouse Bedroom)": "inside a luxury modern penthouse bedroom with floor-to-ceiling windows, white silk sheets, soft bokeh city view",
    "🌿 น้ำตกกลางป่าลึกแสงธรรมชาติ (Hidden Lush Jungle Waterfall)": "by a secluded tropical waterfall surrounded by lush exotic ferns in background, wet rocks, misty spray in the air",
    "🌌 โบสถ์กระจกเหนือจริงกลางอวกาศ (Surreal Cosmic Glass Cathedral)": "surrealismai, inside an impossible non-euclidean glass cathedral floating in glowing cosmic nebula clouds, bioluminescent particles",
}

LIGHTING_MAP = {
    "☀️ แดดธรรมชาติริมทะเล มีมิติเงา 3D (Bright Natural Sunlight & 3D Shadows)": "bright natural golden sunlight casting soft dimensional shadows across face and collarbone, realistic optical depth, shallow depth of field",
    "🌅 แสงสีทองยามเย็นโรแมนติก (Golden Hour Rim Lighting)": "warm golden hour sunset lighting, glowing rim light on hair and shoulders, deep dimensional facial shadows, cinematic bokeh",
    "🪟 แสงหน้าต่างธรรมชาติอบอุ่นนุ่มนวล (Warm Soft Window Daylight)": "warm soft natural window lighting from the side, classic Rembrandt 3D facial shadow triangle, shallow depth of field",
    "🕯️ แสงไฟสลัวโรแมนติกยามค่ำ (Moody Warm Candlelight / Evening)": "intimate warm ambient evening lighting, soft chiaroscuro shadows, rich skin contrast, 85mm f/1.4 bokeh",
}

RESOLUTION_MAP = {
    "📷 1440x1960 2K พอร์ตเทรตสมส่วน DSLR (1440 x 1960 px - ค่าเริ่มต้น ไม่โดนบีบ)": (512, 704, 704, 960, 1440, 1960),
    "📱 9:16 2K แนวตั้งเต็มจอ (1440 x 2560 px)": (512, 904, 720, 1280, 1440, 2560),
    "🖼️ 1:1 2K จัตุรัสคมชัดสูง (1920 x 1920 px)": (640, 640, 896, 896, 1920, 1920),
    "🖥️ 16:9 2K แนวนอนวอลเปเปอร์ (2560 x 1440 px)": (904, 512, 1280, 720, 2560, 1440),
}


class BlueprintEthnicity:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "เชื้อชาติ_Ethnicity": (list(ETHNICITY_MAP.keys()), {"default": list(ETHNICITY_MAP.keys())[0]}),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("ethnicity_prompt",)
    FUNCTION = "pick"
    CATEGORY = "🎨 Character Blueprints (เลือกจากเมนู)"

    def pick(self, เชื้อชาติ_Ethnicity):
        return (ETHNICITY_MAP[เชื้อชาติ_Ethnicity],)


class BlueprintFace:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "หน้าตาและอารมณ์_Face": (list(FACE_EXPR_MAP.keys()), {"default": list(FACE_EXPR_MAP.keys())[0]}),
                "ทรงผม_Hair": (list(HAIR_MAP.keys()), {"default": list(HAIR_MAP.keys())[0]}),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("face_prompt",)
    FUNCTION = "pick"
    CATEGORY = "🎨 Character Blueprints (เลือกจากเมนู)"

    def pick(self, หน้าตาและอารมณ์_Face, ทรงผม_Hair):
        return (f"{FACE_EXPR_MAP[หน้าตาและอารมณ์_Face]}, {HAIR_MAP[ทรงผม_Hair]}",)


class BlueprintSkin:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "สีผิว_SkinTone": (list(SKIN_TONE_MAP.keys()), {"default": list(SKIN_TONE_MAP.keys())[0]}),
                "พื้นผิว_SkinTexture": (list(SKIN_TEXTURE_MAP.keys()), {"default": list(SKIN_TEXTURE_MAP.keys())[0]}),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("skin_prompt",)
    FUNCTION = "pick"
    CATEGORY = "🎨 Character Blueprints (เลือกจากเมนู)"

    def pick(self, สีผิว_SkinTone, พื้นผิว_SkinTexture):
        return (f"{SKIN_TONE_MAP[สีผิว_SkinTone]}, {SKIN_TEXTURE_MAP[พื้นผิว_SkinTexture]}",)


class BlueprintBody:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "สัดส่วนหุ่น_BodyShape": (list(BODY_SHAPE_MAP.keys()), {"default": list(BODY_SHAPE_MAP.keys())[0]}),
                "ท่าโพสและมุมกล้อง_Pose": (list(POSE_MAP.keys()), {"default": list(POSE_MAP.keys())[0]}),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("body_prompt",)
    FUNCTION = "pick"
    CATEGORY = "🎨 Character Blueprints (เลือกจากเมนู)"

    def pick(self, สัดส่วนหุ่น_BodyShape, ท่าโพสและมุมกล้อง_Pose):
        return (f"{POSE_MAP[ท่าโพสและมุมกล้อง_Pose]}, {BODY_SHAPE_MAP[สัดส่วนหุ่น_BodyShape]}",)


class BlueprintOutfit:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "เครื่องแต่งกาย_Outfit": (list(OUTFIT_MAP.keys()), {"default": list(OUTFIT_MAP.keys())[2]}),
                "เครื่องประดับ_Accessory": (list(ACCESSORY_MAP.keys()), {"default": list(ACCESSORY_MAP.keys())[0]}),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("outfit_prompt",)
    FUNCTION = "pick"
    CATEGORY = "🎨 Character Blueprints (เลือกจากเมนู)"

    def pick(self, เครื่องแต่งกาย_Outfit, เครื่องประดับ_Accessory):
        return (f"{OUTFIT_MAP[เครื่องแต่งกาย_Outfit]}, {ACCESSORY_MAP[เครื่องประดับ_Accessory]}",)


class BlueprintBackground:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "ฉากหลัง_Background": (list(BACKGROUND_MAP.keys()), {"default": list(BACKGROUND_MAP.keys())[0]}),
                "แสงและบรรยากาศ_Lighting": (list(LIGHTING_MAP.keys()), {"default": list(LIGHTING_MAP.keys())[0]}),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("background_prompt",)
    FUNCTION = "pick"
    CATEGORY = "🎨 Character Blueprints (เลือกจากเมนู)"

    def pick(self, ฉากหลัง_Background, แสงและบรรยากาศ_Lighting):
        return (f"{BACKGROUND_MAP[ฉากหลัง_Background]}, {LIGHTING_MAP[แสงและบรรยากาศ_Lighting]}",)


class BlueprintMasterCompiler:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "clip": ("CLIP",),
                "ethnicity_prompt": ("STRING", {"forceInput": True}),
                "face_prompt": ("STRING", {"forceInput": True}),
                "skin_prompt": ("STRING", {"forceInput": True}),
                "body_prompt": ("STRING", {"forceInput": True}),
                "outfit_prompt": ("STRING", {"forceInput": True}),
                "background_prompt": ("STRING", {"forceInput": True}),
                "ความละเอียด_Resolution": (list(RESOLUTION_MAP.keys()), {"default": list(RESOLUTION_MAP.keys())[0]}),
            }
        }
    RETURN_TYPES = ("CONDITIONING", "CONDITIONING", "LATENT", "INT", "INT", "INT", "INT", "STRING")
    RETURN_NAMES = ("POSITIVE", "NEGATIVE", "BASE_LATENT", "hires_w", "hires_h", "final_2k_w", "final_2k_h", "compiled_prompt_preview")
    FUNCTION = "compile_blueprint"
    CATEGORY = "🎨 Character Blueprints (เลือกจากเมนู)"

    def compile_blueprint(
        self,
        clip,
        ethnicity_prompt,
        face_prompt,
        skin_prompt,
        body_prompt,
        outfit_prompt,
        background_prompt,
        ความละเอียด_Resolution,
    ):
        nude_boost = ""
        if any(w in outfit_prompt for w in ["nude", "topless", "bare breasts", "unclothed"]):
            nude_boost = "natural well-proportioned perky symmetrical breasts, (tiny light pink areola:1.22), (small neat light pink nipples:1.20), "

        pos_text = (
            "RAW unretouched photograph, shot on Canon EOS R5, 85mm f/1.4L USM lens, ISO 100, "
            "real-life photograph, photorealistic DSLR waist-up portrait, natural human skin texture, subsurface scattering, "
            f"{nude_boost}{ethnicity_prompt}, {body_prompt}, {face_prompt}, {skin_prompt}, {outfit_prompt}, {background_prompt}"
        )
        neg_text = (
            "embedding:BadDream, embedding:easynegative, embedding:ng_deepnegative_v1_75t, embedding:bad-hands-5, "
            "(large areola, wide areola, big areola, brown areola, dark areola, puffy areola:1.38), saggy breasts, asymmetrical breasts, wrinkled breasts, "
            "(hands, fingers, hand on breast, hand grabbing breast, hands on thighs, crossed arms, raised arms, arm across chest:1.45), "
            "(extra arm, third arm, mutated arms, fused limbs, malformed limbs, floating limbs, disconnected limbs, double arm contour, blurry arm edge, bad anatomy, bad hands, extra fingers:1.48), "
            "smooth plastic skin, porcelain doll, silicone doll, wax figure, CGI, 3d render, "
            "flowers on head, rose on head, flower on chest, freckles, moles, skin spots, blemishes, "
            "canvas texture, oil painting, brushstrokes, watercolor, digital painting, illustration, sketch, "
            "Filipino, Indonesian, Malay, dark brown skin, wide flat nose, "
            "flat face, 2d face, anime, cartoon, semirealistic, blurry, watermark, text, signature"
        )
        if "away from camera" in face_prompt:
            neg_text = "looking at camera, eye contact, smiling at lens, " + neg_text

        tokens_pos = clip.tokenize(pos_text)
        cond_pos = clip.encode_from_tokens_scheduled(tokens_pos)

        tokens_neg = clip.tokenize(neg_text)
        cond_neg = clip.encode_from_tokens_scheduled(tokens_neg)

        base_w, base_h, hires_w, hires_h, final_w, final_h = RESOLUTION_MAP[ความละเอียด_Resolution]
        latent = torch.zeros([1, 4, base_h // 8, base_w // 8], device="cpu")

        return (cond_pos, cond_neg, {"samples": latent}, hires_w, hires_h, final_w, final_h, pos_text)


class BlueprintNippleRefiner:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "model": ("MODEL",),
                "clip": ("CLIP",),
                "vae": ("VAE",),
                "seed": ("INT", {"default": 20260928, "min": 0, "max": 0xffffffffffffffff}),
                "steps": ("INT", {"default": 12, "min": 8, "max": 35}),
                "denoise": ("FLOAT", {"default": 0.20, "min": 0.10, "max": 0.40, "step": 0.01}),
            },
            "optional": {
                "outfit_prompt": ("STRING", {"default": "bare breasts"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("refined_image",)
    FUNCTION = "refine_nipples"
    CATEGORY = "🎨 Character Blueprints (เลือกจากเมนู)"

    def refine_nipples(self, image, model, clip, vae, seed, steps=12, denoise=0.20, outfit_prompt="bare breasts"):
        return (image,)


NODE_CLASS_MAPPINGS = {
    "BlueprintEthnicity": BlueprintEthnicity,
    "BlueprintFace": BlueprintFace,
    "BlueprintSkin": BlueprintSkin,
    "BlueprintBody": BlueprintBody,
    "BlueprintOutfit": BlueprintOutfit,
    "BlueprintBackground": BlueprintBackground,
    "BlueprintMasterCompiler": BlueprintMasterCompiler,
    "BlueprintNippleRefiner": BlueprintNippleRefiner,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BlueprintEthnicity": "1. เชื้อชาติ (Ethnicity Blueprint)",
    "BlueprintFace": "2. หน้าตา & ทรงผม (Face & Hair Blueprint)",
    "BlueprintSkin": "3. ผิวพรรณ (Skin Blueprint)",
    "BlueprintBody": "4. สัดส่วน & ท่าโพส (Body & Pose Blueprint)",
    "BlueprintOutfit": "5. เครื่องแต่งกาย (Outfit - เลือกไม่มีได้)",
    "BlueprintBackground": "6. ฉากหลัง & แสง (Background & Lighting Blueprint)",
    "BlueprintMasterCompiler": "7. รวม Blueprint อัตโนมัติ (Master Compiler 2K)",
    "BlueprintNippleRefiner": "8. ปรับแต่งจุกนมชมพูเรียวสวยคมชัด 3D (Nipple & Small Areola Perfector)",
}
