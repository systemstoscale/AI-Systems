---
module_id: images
module_name: Image Generation
module_number: 12
category: business
description: AI image generation for brand assets, thumbnails, ad creatives
env_keys:
  required:
    - key: OPENAI_API_KEY
      label: OpenAI API Key
      get_url: https://platform.openai.com/api-keys
      hint: "Starts with sk-. For GPT Image / DALL-E"
  optional:
    - key: REPLICATE_API_TOKEN
      label: Replicate API Token
      get_url: https://replicate.com/account/api-tokens
      hint: "For Flux models. Starts with r8_"
pip_packages: [python-dotenv, requests]
test_command: null
estimated_time: "15 minutes"
interactive_steps: true
---

# Instruction: Image Generation Setup

## Goal
Set up AI image generation for brand assets, social media visuals, ad creatives, and thumbnails. End state: the user can request images in their brand style and get consistent, on-brand visuals without a designer.

## Inputs
- `brand_colors` (list): Primary, secondary, accent colors (hex codes)
- `brand_fonts` (list, optional): Font names used in branding
- `style_references` (list, optional): URLs or files of images that represent the desired aesthetic
- `use_cases` (list): What images are needed for — "social_posts", "thumbnails", "ads", "blog_headers", "presentations"
- `image_provider` (string): "openai" (GPT Image / DALL-E), "midjourney", "flux", or "stable_diffusion"

## Steps

### 1. Choose your image provider

| Provider | Best For | Cost | API Available |
|----------|----------|------|---------------|
| GPT Image (OpenAI) | General purpose, text in images, quick iteration | Pay per image | Yes |
| Midjourney | Photorealistic, artistic, highest quality | $10-60/mo subscription | Via Discord bot or API |
| Flux (Replicate) | Open source, customizable, fine-tuning | Pay per generation | Yes |
| Stable Diffusion | Local generation, full control, free | Free (GPU required) | Self-hosted |

**Recommendation:** Start with GPT Image via OpenAI API. Fastest to set up, good quality for business use cases, and supports text rendering.

### 2. Set up the API connection

**GPT Image / DALL-E (OpenAI):**
1. Get API key at platform.openai.com
2. Add to `.env`:
   ```
   OPENAI_API_KEY=sk-...
   ```
3. Test with a simple generation call

**Flux (via Replicate):**
1. Get API token at replicate.com
2. Add to `.env`:
   ```
   REPLICATE_API_TOKEN=r8_...
   ```

### 3. Create the brand style guide

Document the visual brand in `context/brand-style.md`:

```markdown
# Brand Style Guide

## Colors
- Primary: #XXXXXX (name)
- Secondary: #XXXXXX (name)
- Accent: #XXXXXX (name)
- Background: #XXXXXX
- Text: #XXXXXX

## Typography
- Headlines: [Font name]
- Body: [Font name]

## Visual Style
- [Describe the aesthetic: minimal, bold, corporate, playful, etc.]
- [Photo style: lifestyle, studio, illustrated, abstract]
- [Mood: professional, energetic, calm, edgy]

## Do's
- [Things that represent the brand well]

## Don'ts
- [Things to avoid — stock photo vibes, certain colors, etc.]
```

### 4. Build prompt templates

Create `instructions/image-prompts.md` with reusable prompt templates:

**Social media post image:**
```
[Subject description]. Professional, modern design with [brand color] accent colors.
Clean composition, [style] aesthetic. Social media format, high contrast,
easy to read at small sizes. No text overlay.
```

**YouTube thumbnail:**
```
[Subject/person description]. Bold, eye-catching thumbnail style.
[Brand color] background or accent. High contrast, dramatic lighting.
Close-up composition, expressive. Space on [left/right] for text overlay.
16:9 aspect ratio.
```

**Ad creative:**
```
[Product/service visualization]. Clean, premium feel. [Brand color] color scheme.
Lifestyle context showing [target audience]. Professional photography style.
[Square/portrait/landscape] format for [platform].
```

**Blog/article header:**
```
[Topic visualization]. Minimalist, modern design. [Brand color] palette.
Abstract or conceptual representation. Wide format (16:9),
suitable as a blog header image. Subtle, not distracting from text.
```

### 5. Create the generation script

Create `scripts/generate-image.py` that:
1. Takes a prompt and use case (social, thumbnail, ad, blog)
2. Applies the brand style template automatically
3. Generates the image via chosen provider
4. Saves to `outputs/images/[use-case]-[YYYY-MM-DD]-[N].png`
5. Logs the prompt used (for consistency and iteration)

```python
# Usage examples:
# python scripts/generate-image.py --type thumbnail --prompt "person excited about AI automation"
# python scripts/generate-image.py --type social --prompt "data dashboard on laptop screen"
# python scripts/generate-image.py --type ad --prompt "business owner saving time with automation"
```

**Size presets by use case:**

| Use Case | Size | Aspect Ratio |
|----------|------|--------------|
| Instagram post | 1080x1080 | 1:1 |
| Instagram story | 1080x1920 | 9:16 |
| Facebook ad | 1200x628 | ~1.9:1 |
| YouTube thumbnail | 1280x720 | 16:9 |
| LinkedIn post | 1200x627 | ~1.9:1 |
| Twitter/X post | 1200x675 | 16:9 |
| Blog header | 1200x630 | ~1.9:1 |

### 6. Set up thumbnail generation (if YouTube)

If the user creates YouTube content, build a specialized thumbnail workflow:

1. Read the video title and script
2. Generate 3 thumbnail concepts:
   - **Concept A**: Emotion-focused (face close-up with dramatic expression)
   - **Concept B**: Result-focused (before/after, dashboard, outcome)
   - **Concept C**: Curiosity-focused (abstract, intriguing visual)
3. Generate each with the image API
4. Add text overlay using Python PIL/Pillow (if needed)
5. Save all 3 for A/B testing

### 7. Set up batch generation (optional)

For users who need multiple images regularly, create `scripts/batch-images.py`:
1. Read a CSV or list of prompts
2. Generate all images with rate limiting
3. Organize in `outputs/images/[campaign-name]/`
4. Generate a preview HTML page for easy review

### 8. Test the pipeline

1. [ ] API key works and generates an image
2. [ ] Brand style guide accurately represents the user's brand
3. [ ] Prompt templates produce consistent, on-brand results
4. [ ] Images save to correct output directory
5. [ ] Size presets match platform requirements
6. [ ] User approves the visual quality and style

## Script
- `scripts/generate-image.py` — Single image generation with brand templates
- `scripts/batch-images.py` — Batch generation for campaigns (optional)

## Output
- `outputs/images/` — Generated images organized by use case
- `context/brand-style.md` — Visual brand guide
- `instructions/image-prompts.md` — Reusable prompt templates

## Requirements
- `OPENAI_API_KEY` in `.env` (for GPT Image / DALL-E) or alternative provider key
- Python 3, `requests` library
- `Pillow` library (optional, for text overlays on thumbnails)
- Brand colors and style direction from the user

## Edge Cases
- **User has no brand guidelines**: Create basic ones during setup. Ask for 2-3 colors they like, show examples, pick a style direction.
- **Images don't match brand**: Refine prompts by adding more specific style descriptors. "Corporate minimalism" vs "startup energy" produce very different results.
- **Text in images**: DALL-E/GPT Image handles short text fairly well. For longer text or precise typography, generate the image without text and overlay with Pillow.
- **Consistency across images**: Use the same style suffix in every prompt. Save working prompts as templates.
- **Provider rate limits**: OpenAI: 50 images/minute on most tiers. Replicate: varies by model. Add delays for batch jobs.
- **Cost management**: GPT Image: ~$0.04-0.08 per image. Set a monthly image budget. Log all generations with cost.

## Notes
- Image generation is an art. First attempts rarely hit the mark. Iterate on prompts, save winners.
- The best thumbnails combine AI-generated backgrounds with real photos of the user (composite in Canva or Figma).
- Consistency matters more than perfection. A cohesive feed with "good enough" images beats random beautiful ones.
- After each batch, update prompt templates with what worked best.
