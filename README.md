# Beat-Synced AI Film Skill

A reusable creative-production workflow for AI music videos, psychedelic self-portraits, beat-driven motion design and After Effects refinement. It connects reference research, identity-consistent storyboards, physically readable generation prompts, credit-aware tests, speed ramps, tracked VFX, cover art and verified delivery.

Created from an iterative short-film production process. The distinctive lesson is continuity: the body, camera, effects and edit must tell the same motion story. The package includes no personal photographs, music, generated footage, account information or private project files.

## Use it

**Codex:** copy the `beat-synced-ai-film` directory into your configured skills directory, usually `~/.codex/skills/`. Start a chat that loads installed skills and invoke `$beat-synced-ai-film`. Automatic selection is also enabled through its description.

```bash
git clone https://github.com/11vinaypathak-sys/beat-synced-ai-film-skill.git
mkdir -p ~/.codex/skills
cp -R beat-synced-ai-film-skill/beat-synced-ai-film ~/.codex/skills/
```

If that skill is already installed, review and replace its existing folder deliberately rather than nesting a second copy. You can also give a compatible skill installer [this repository URL](https://github.com/11vinaypathak-sys/beat-synced-ai-film-skill) and the skill path `beat-synced-ai-film`.

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

## Discovery and sharing

The installable skill has a capability-specific name, trigger description and UI metadata. This README provides natural-language examples and direct links to the detailed procedures so people and AI tools can identify the right entry point.

Repository: [11vinaypathak-sys/beat-synced-ai-film-skill](https://github.com/11vinaypathak-sys/beat-synced-ai-film-skill).

This repository contains reusable instructions, templates and a verification helper. It does not include the originating film, personal portraits, music, commercial fonts, credentials or private production files. It works with available generation providers and MCP or application-control integrations; it does not install those integrations or grant account access.

The public README, skill metadata and topic tags help people and compatible agents identify its purpose. Public hosting does not guarantee search-engine indexing, automatic retrieval by every AI assistant or inclusion in any skill registry.

## License

The authored instructions, templates and helper code are MIT licensed; see [LICENSE](LICENSE). Third-party tools, fonts, media and linked reference artwork retain their own licenses. No reference images or commercial fonts are redistributed here.
