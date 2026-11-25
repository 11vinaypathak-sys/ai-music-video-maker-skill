# AI Music Video Maker

A **general production workflow** for turning your own idea and music into an original short AI video or visual Reel.

This public starter covers **brief → storyboard → test shot → rough edit → review → export**. It does not include the creator’s project-specific prompts, signature motion recipes, compositing settings, timing maps or source media. It is not an exact-recreation kit for a demonstration film.

## Try it

Copy the [starter prompt](beat-synced-ai-film/PROMPT.md) into an assistant with media tools. Supply your idea, music you can use, desired length, format and budget.

Example: “Help me plan a short AI music video around my idea. Show a storyboard, then test one shot before making the full sequence.”

## Install in Codex

Copy `beat-synced-ai-film` into your skills directory and invoke `$beat-synced-ai-film`. The existing skill name is retained for compatibility.

```bash
git clone https://github.com/11vinaypathak-sys/ai-music-video-maker-skill.git
mkdir -p ~/.codex/skills
cp -R ai-music-video-maker-skill/beat-synced-ai-film ~/.codex/skills/
```

For an existing installation, back it up and replace the folder deliberately; merging folders can leave obsolete reference files behind.

## Included

- [General workflow](beat-synced-ai-film/SKILL.md)
- [Portable starter prompt](beat-synced-ai-film/PROMPT.md)
- [Project brief and storyboard skeleton](beat-synced-ai-film/references/project-brief.md)
- [Optional media verification helper](beat-synced-ai-film/scripts/verify_media.py)

The helper requires Python 3, ffmpeg and ffprobe. It inspects media and can verify archive integrity; it does not generate footage or certify creative quality.

```bash
python3 beat-synced-ai-film/scripts/verify_media.py --help
```

Generation and editing depend on your available tools and may incur provider costs. Bring your own authorized assets. No subscriptions, credits, personal imagery or music are included. No specific visual result or social-media reach is promised.

For editing existing travel footage, see [Travel Reel Editor](https://github.com/11vinaypathak-sys/travel-reel-editor-skill).

## License

Public instructions and helper code are MIT licensed; see [LICENSE](LICENSE). Third-party tools and media retain their respective terms.
