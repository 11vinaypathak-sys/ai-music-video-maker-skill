# AI Music Video Maker

**Turn an idea and a music track into a short AI music video, with scenes, effects and cuts timed to the music.**

A reusable **Codex skill + copy-paste prompt** for AI-assisted video production. It guides storyboards, consistent characters, generated footage, beat-synced editing, cover art and export checks. Rendering and generation use the tools connected to your assistant.

**You bring:** your idea, music you can use, visual references, desired length and any generation budget. Add an approved portrait if the film features you.

**You can make:** a short music video or visual Reel, plus a cover and editable project when requested and supported by your tools. Personal portraits, music and footage are not included in this repository.

## Start here

- **Try it in a chat:** copy the [ready-to-use prompt](beat-synced-ai-film/PROMPT.md), add your brief and attach your own assets. No skill installation is needed; generation and editing still need suitable tools.
- **Use it in Codex:** follow the installation steps below, then invoke `$beat-synced-ai-film`.
- **Already have travel footage?** Use [Travel Reel Editor](https://github.com/11vinaypathak-sys/travel-reel-editor-skill) to shape existing clips and photos into a film.

Try asking: “Help me make a 30-second AI music video from this idea and track. Show me the storyboard first, then test one shot within my budget.”

## Install in Codex

Copy the `beat-synced-ai-film` directory into your configured skills directory, usually `~/.codex/skills/`. Start a chat that loads installed skills and invoke `$beat-synced-ai-film`. The existing skill ID stays `beat-synced-ai-film`, so current installations and prompts keep working.

```bash
git clone https://github.com/11vinaypathak-sys/ai-music-video-maker-skill.git
mkdir -p ~/.codex/skills
cp -R ai-music-video-maker-skill/beat-synced-ai-film ~/.codex/skills/
```

If that skill is already installed, review and replace its existing folder deliberately rather than nesting a second copy. You can also give a compatible skill installer [this repository URL](https://github.com/11vinaypathak-sys/ai-music-video-maker-skill) and the skill path `beat-synced-ai-film`.

**Other assistants:** use the [portable prompt](beat-synced-ai-film/PROMPT.md), then provide your own references and assets. For deeper work, include the relevant reference documents. A prompt cannot install tools or give an assistant account access.

Example requests:

- “Create a 28-second AI self-portrait music video with calm body movement, fast moving colour layers and beat-synced cuts.”
- “Continue this exact airborne pose into a rear energy impact and immediate pullback; show one raw take within my stated budget.”
- “Fix the eye transition and shoe speed ramp in my existing After Effects cut without regenerating footage.”
- “Research Pinterest cover references first, then create a minimal prismatic portrait cover using my approved face.”
- “Collect the editable project and verify the final film before packaging.”
- “Keep my landscape film inside a vertical Reel with a static carved-black surround. Show a still first, then export with the original music.”

This is not a one-click video generator, a model subscription, a stock-media license or a promise of social-media reach. It adapts to the host's available tools. Provider pricing, APIs and platform upload requirements must be checked at execution time.

## What's inside

| Resource | Purpose |
|---|---|
| [SKILL.md](beat-synced-ai-film/SKILL.md) | Discoverable workflow and decision criteria |
| [Beat and continuity](beat-synced-ai-film/references/beat-and-continuity.md) | Audio evidence, markers, match frames and retiming |
| [Motion and prompts](beat-synced-ai-film/references/motion-and-prompts.md) | Body/camera/effect choreography, impact example and credit ledger |
| [After Effects and QA](beat-synced-ai-film/references/after-effects-and-qa.md) | Tracking, local corrections, render and package verification |
| [Covers and references](beat-synced-ai-film/references/covers-and-references.md) | Actual-reference research, prism/cutout distinction, typography |
| [Reel presentation](beat-synced-ai-film/references/reel-presentation.md) | Static optical depth, wide-film preservation, background isolation and social packaging |
| [Production template](beat-synced-ai-film/references/production-template.md) | Compact project, shot and generation record |
| [Verification helper](beat-synced-ai-film/scripts/verify_media.py) | Read-only media inspection and optional ZIP CRC test |

## Local verification helper

Requires Python 3, `ffprobe` and `ffmpeg` on PATH. No Python packages, network access or API keys are needed.

```bash
python3 beat-synced-ai-film/scripts/verify_media.py final.mp4 --expected-duration 28 --require-audio --zip delivery.zip --report qa.json
```

It probes and fully decodes the video, reports black intervals and audio loudness/peak, and optionally tests a ZIP. Black intervals trigger review warnings rather than automatic failure because black may be intentional. A successful technical report does not prove creative quality, audio synchronization, asset licensing or After Effects portability.

## Sharing and discovery

The installable skill has a capability-specific name, trigger description and UI metadata. This README provides natural-language examples and direct links to the detailed procedures so people and AI tools can identify the right entry point.

Repository: [11vinaypathak-sys/ai-music-video-maker-skill](https://github.com/11vinaypathak-sys/ai-music-video-maker-skill).

This repository contains reusable instructions, templates and a verification helper. It does not include the originating film, personal portraits, music, commercial fonts, credentials or private production files. It works with available generation providers and MCP or application-control integrations; it does not install those integrations or grant account access.

The public README, skill metadata and topic tags help people and compatible agents identify its purpose. Public hosting does not guarantee search-engine indexing, automatic retrieval by every AI assistant or inclusion in any skill registry.

## License

The authored instructions, templates and helper code are MIT licensed; see [LICENSE](LICENSE). Third-party tools, fonts, media and linked reference artwork retain their own licenses. No reference images or commercial fonts are redistributed here.
