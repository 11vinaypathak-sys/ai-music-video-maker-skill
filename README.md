# AI Music Video Maker

**An art-direction-led workflow by Vinay Pathak for turning an idea, a track and visual references into an original AI music video.**

Developed through my work across design, motion and AI-assisted filmmaking. The process starts with the feeling a film should create, builds a visual direction around it, and uses small tests and specific feedback to shape the finished piece.

**Idea → visual research → art direction → storyboard → motion test → edit → finishing**

## How it works

- **Find the direction.** Turn an initial thought into a clear creative brief. Explore references for composition, atmosphere and storytelling.
- **Make it tangible.** Develop a storyboard and test a representative shot before expanding production.
- **Refine through feedback.** Translate “this feels off” into a concrete revision to pacing, framing, imagery or sound.
- **Finish the piece.** Assemble the cut, review it against the brief and check the export.

The tools serve the direction. Use available image and video generators, editing applications and MCP connections where they fit the task. The assistant checks which capabilities are actually connected before planning production.

## Bring your idea

Supply your concept, music you can use, visual references, intended format and budget. If a project already exists, include the latest version so the workflow can build on it.

Try: “I want to turn this track and idea into a visual Reel. Help me find a direction, show a storyboard and test one shot before developing the full edit.”

[**Use the creative brief prompt**](beat-synced-ai-film/PROMPT.md)

## Install in Codex

Copy `beat-synced-ai-film` into your skills directory and invoke `$beat-synced-ai-film`.

```bash
git clone https://github.com/11vinaypathak-sys/ai-music-video-maker-skill.git
mkdir -p ~/.codex/skills
cp -R ai-music-video-maker-skill/beat-synced-ai-film ~/.codex/skills/
```

If already installed, back up and replace the existing folder deliberately instead of merging old reference files into the new version. The skill identifier remains unchanged.

## Inside the workflow

- [Skill instructions](beat-synced-ai-film/SKILL.md)
- [Creative brief prompt](beat-synced-ai-film/PROMPT.md)
- [Direction and storyboard worksheet](beat-synced-ai-film/references/project-brief.md)
- [Media verification helper](beat-synced-ai-film/scripts/verify_media.py)

The optional helper requires Python 3, ffmpeg and ffprobe. It checks file integrity and technical properties; creative review happens through watching and listening.

```bash
python3 beat-synced-ai-film/scripts/verify_media.py --help
```

Generation and editing require suitable tools and your own authorized assets. Provider charges are separate; agree a budget before production. Outputs depend on the brief, source material, tools and creative decisions.

Working with existing travel footage? See [Travel Reel Editor](https://github.com/11vinaypathak-sys/travel-reel-editor-skill).

Created by **Vinay Pathak** · [Portfolio](https://11vinaypathak-sys.github.io/portfolio/) · [Behance](https://www.behance.net/1vinaypathak)

## License

Public instructions and helper code are MIT licensed; see [LICENSE](LICENSE). Third-party tools and media retain their respective terms.
