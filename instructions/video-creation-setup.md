---
module_id: video
module_name: Video Creation
module_number: 13
category: business
description: AI-assisted video pipeline — scripts, voiceover, avatar, editing
env_keys:
  required: []
  optional:
    - key: ELEVENLABS_API_KEY
      label: ElevenLabs API Key
      get_url: https://elevenlabs.io
      hint: "For voice cloning and AI voiceover"
    - key: HEYGEN_API_KEY
      label: HeyGen API Key
      get_url: https://heygen.com
      hint: "For AI avatar videos"
    - key: OPENAI_API_KEY
      label: OpenAI API Key
      get_url: https://platform.openai.com/api-keys
      hint: "For Whisper transcription and TTS"
pip_packages: [python-dotenv, requests]
system_packages:
  - name: ffmpeg
    install_mac: "brew install ffmpeg"
    install_linux: "sudo apt install ffmpeg"
test_command: null
estimated_time: "30 minutes"
interactive_steps: true
---

# Instruction: Video Creation Setup

## Goal
Set up an AI-assisted video creation pipeline: generate scripts, create or edit videos with AI tools, add voiceovers, and publish. End state: the user can go from idea to published video with minimal manual editing.

## Inputs
- `video_type` (string): "talking_head", "screen_share", "ai_avatar", "mixed", "shorts"
- `publish_platform` (list): "youtube", "tiktok", "instagram_reels", "linkedin_video"
- `voice_source` (string): "user_records", "ai_voice" (ElevenLabs/OpenAI TTS), "ai_avatar" (HeyGen)
- `editing_style` (string): "minimal", "jump_cut", "b_roll_heavy", "tutorial"

## Steps

### 1. Assess the user's video workflow

Ask the user:
1. Do you currently record yourself on camera?
2. Do you have video editing experience? (None / Basic / Advanced)
3. What equipment do you have? (Phone / Webcam / Camera + mic)
4. How long should your videos be? (Shorts: 30-60s, Standard: 8-15min, Long: 20min+)
5. Do you want AI avatars (you don't appear on camera) or AI-assisted editing (you record, AI edits)?

This determines which tools to set up.

### 2. Set up script generation

Use the content pipeline module (`instructions/content-pipeline-setup.md`) for scripts, or create a standalone:

Create `instructions/video-script.md` with the structure:
```
HOOK (0:00-0:30)
[Grab attention — bold statement, question, or shocking fact]

INTRO (0:30-1:00)
[Quick context — why this matters, what they'll learn]

SECTION 1 (1:00-3:00)
[First key point with example/story]

SECTION 2 (3:00-5:00)
[Second key point with proof/data]

SECTION 3 (5:00-7:00)
[Third key point with actionable takeaway]

CTA (7:00-8:00)
[What to do next — subscribe, comment, link]
```

### 3. Set up AI voice (if applicable)

**ElevenLabs (voice cloning):**
1. Create account at elevenlabs.io
2. Upload 3-5 minutes of the user's clean audio (podcast, video, voice memo)
3. Clone voice → get `voice_id`
4. Add to `.env`:
   ```
   ELEVENLABS_API_KEY=your_key
   ELEVENLABS_VOICE_ID=your_cloned_voice_id
   ```
5. Create `scripts/generate-voiceover.py`:
   - Takes script text input
   - Generates audio via ElevenLabs API
   - Saves to `outputs/audio/voiceover-[YYYY-MM-DD].mp3`

**OpenAI TTS (no cloning, preset voices):**
1. Use existing `OPENAI_API_KEY` from `.env`
2. Choose a voice: `alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer`
3. Cheaper but no custom voice cloning

### 4. Set up AI avatar (if applicable)

**HeyGen (AI avatar videos):**
1. Create account at heygen.com
2. Upload the user's video to create a personal avatar (or use stock avatars)
3. Add to `.env`:
   ```
   HEYGEN_API_KEY=your_key
   HEYGEN_AVATAR_ID=your_avatar_id
   ```
4. Create `scripts/create-avatar-video.py`:
   - Takes script text
   - Generates video with avatar speaking the script
   - Supports multiple backgrounds and outfits
   - Downloads completed video to `outputs/video/`

**HeyGen workflow:**
```
Script → API: create video task → Poll for completion (5-15 min) → Download MP4
```

### 5. Set up video editing automation

**For users who record themselves:**

Create `scripts/edit-video.py` that automates common editing tasks:

**Jump cut editing:**
- Detect and remove silences (voice activity detection)
- Remove filler words (um, uh, like)
- Add padding around cuts for natural feel

**B-roll insertion:**
- Identify moments where b-roll would help (screen shares, examples)
- Mark timestamps in the script for b-roll insertion

**Caption generation:**
- Transcribe audio using Whisper (OpenAI)
- Generate SRT subtitle file
- Style captions for each platform (TikTok style = bold, centered, animated)

```python
# Pipeline:
# 1. Transcribe raw footage
# 2. Detect silences and filler words
# 3. Generate edit decision list (EDL)
# 4. Apply cuts (ffmpeg)
# 5. Generate captions
# 6. Export final video + SRT
```

**Tools needed:**
- `ffmpeg` for video processing
- `whisper` (OpenAI) for transcription
- Python `moviepy` or direct `ffmpeg` commands

### 6. Set up thumbnail generation

Link to image generation module (`instructions/image-generation-setup.md`):
- Generate 3 thumbnail concepts per video
- A/B test thumbnails after 24 hours
- Track CTR to find winning formats

### 7. Set up publishing

**YouTube upload (automated):**
1. Set up Google OAuth (see `scripts/connections.py`)
2. Create `scripts/upload-youtube.py`:
   - Upload video file
   - Set title, description, tags, thumbnail
   - Set privacy (unlisted → public after review)
   - Add to playlist

**Multi-platform publishing:**
- YouTube: Full video (8-15 min)
- TikTok/Reels/Shorts: Cut key moments to 30-60s clips
- LinkedIn: Upload directly (native video gets more reach)

Create `scripts/create-clips.py` that:
1. Takes a long-form video
2. Identifies the best 3-5 clip-worthy moments (based on script sections)
3. Cuts clips with ffmpeg
4. Resizes to 9:16 for vertical platforms
5. Adds captions

### 8. Create the video production workflow

Document the full workflow in `instructions/video-production.md`:

```
Pre-Production (30 min):
1. Pick topic from content calendar
2. Generate or finalize script
3. Set up recording environment

Production (varies):
Option A — Record yourself (30-60 min)
  1. Record talking head / screen share
  2. Run edit-video.py for automated cuts
  3. Add b-roll if needed

Option B — AI Avatar (10 min)
  1. Paste script into HeyGen or run create-avatar-video.py
  2. Wait for generation (5-15 min)
  3. Download and review

Post-Production (20 min):
1. Generate captions
2. Create thumbnail (3 options)
3. Write title + description
4. Upload to YouTube (draft)
5. Create short-form clips for social
6. Schedule everything
```

### 9. Test the pipeline

1. [ ] Script generation produces quality output in the user's voice
2. [ ] AI voice sounds natural (if using ElevenLabs/TTS)
3. [ ] AI avatar video is acceptable quality (if using HeyGen)
4. [ ] Video editing automation correctly removes silences
5. [ ] Captions generate accurately
6. [ ] Clips cut correctly for short-form
7. [ ] Upload to YouTube works (test with unlisted video)

## Script
- `scripts/generate-voiceover.py` — AI voiceover generation
- `scripts/create-avatar-video.py` — HeyGen avatar video (optional)
- `scripts/edit-video.py` — Automated video editing
- `scripts/create-clips.py` — Short-form clip extraction
- `scripts/upload-youtube.py` — YouTube publishing

## Output
- `outputs/audio/` — Generated voiceovers
- `outputs/video/` — Finished videos and clips
- `outputs/captions/` — SRT subtitle files
- `instructions/video-production.md` — Full production workflow

## Requirements
- `ELEVENLABS_API_KEY` + `ELEVENLABS_VOICE_ID` in `.env` (for AI voice)
- `HEYGEN_API_KEY` + `HEYGEN_AVATAR_ID` in `.env` (for AI avatar)
- `OPENAI_API_KEY` in `.env` (for transcription/TTS)
- Google OAuth credentials (for YouTube upload)
- `ffmpeg` installed (`brew install ffmpeg` / `apt install ffmpeg`)
- Python 3, `requests`, `moviepy` (optional)

## Edge Cases
- **User doesn't want to appear on camera**: Use AI avatar (HeyGen) or screen-share only format. Both work well for educational content.
- **Voice clone sounds robotic**: Upload higher quality audio samples. Minimum 3 minutes of clean speech, no background noise.
- **HeyGen avatar looks uncanny**: Use it for informational content (tutorials, updates) where slight imperfection is acceptable. Don't use for emotional/personal content.
- **Long video processing times**: HeyGen can take 15-30 minutes for a 10-minute video. Queue jobs and continue working.
- **ffmpeg not installed**: Guide user through installation. It's required for any video processing.
- **YouTube upload quota**: Default quota is 10,000 units/day. Each upload costs ~1,600 units. That's ~6 uploads/day.

## Notes
- AI avatars are improving rapidly but still look best at 720p with limited gestures. Use for B2B/educational content.
- The highest ROI video workflow: user records 10-minute talking head → auto-edit → generate 3 clips for shorts → publish all from one recording session.
- Always review AI-generated content before publishing. Hallucinations in voiceover and lip sync errors in avatars happen.
- After each production cycle, update this file with timing benchmarks and quality notes.
