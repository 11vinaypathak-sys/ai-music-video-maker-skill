---
name: beat-synced-ai-film
description: Create or refine beat-synced AI music videos, identity-consistent self-portrait films, psychedelic motion effects, and matching Reel covers. Use for storyboard-to-video workflows combining generated footage, speed ramps, impact choreography and After Effects compositing, or for refining a specific shot in that workflow.
---

# Beat-Synced AI Film

Turn a visual idea into a coherent short film: persistent identity, physically readable motion, effects that evolve independently, musical timing and an editable verified delivery. Work in the current assistant and available tools; do not require a particular provider or another AI service.

## Start from the actual state

Find the approved current project, render, references, source identity images, audio excerpt, generated takes and generation receipts. Inspect their contents before rebuilding. Ask only for missing information that changes the next decision. A transcript's claim that a render or beat analysis exists is not proof; verify the artifact.

Establish the current task mode:

- **Explore:** references and visual direction. Show the requested references before generating when the user asks to research first.
- **Storyboard:** spatially and temporally connected image frames.
- **Generate:** one bounded motion test or authorized production take.
- **Refine:** targeted retiming, continuity, tracking or compositing in the existing project.
- **Deliver:** checked exports, collected source, cover and optional posting copy.

User feedback can change one mode without cancelling other authorized work. Do not treat an enthusiastic response as approval for new credit spending, posting, a provider switch or a different reference style.

## Working method

1. **Define invariants.** Record subject identity, hair, glasses, clothing, scene, palette, aspect ratio, motion direction, music boundaries and approved moments. Separate fixed facts from creative hypotheses. Keep one clear editable WIP; use recoverable checkpoints rather than deleting source takes.
2. **Map the music.** Use an available audio file; inspect the waveform, detect candidate transients if useful, and listen. Locate the actual excerpt and ending before assigning precise timestamps. See [beat-and-continuity.md](references/beat-and-continuity.md).
3. **Read references as mechanisms.** Identify the camera path, body response, layer propagation, occlusion, scale and texture that create the effect. Distinguish a refracted photographic surface, a rigid extruded cutout, a flowing ribbon and an additive glow. They are different designs. Name what was actually viewed; do not claim to have watched a clip based only on its thumbnail.
4. **Build connected frames.** Start with an approved identity image and previous shot's final pose. Show the smallest useful set of story states: anticipation, onset, contact, recoil, expansion, recovery. An image per second does not prescribe a cut per second. Storyboards describe action; beat markers drive edit decisions.
5. **Describe independent motion.** Give the body, camera, effects and edit separate instructions, then connect them causally. A still pose may coexist with moving effects. See [motion-and-prompts.md](references/motion-and-prompts.md).
6. **Use a bounded generation loop.** Record provider, exact model/version, source frames, duration, resolution, audio setting and quoted price. Reuse the successful model/settings when continuity matters; verify current availability and cost. Submit only within the user's authorized scope and total cap. Show a requested raw take before integration. Do not retry a submission of uncertain status until its job or charge is checked.
7. **Refine one defect at a time.** Translate feedback into an observable change. Review a short section before the full cut when requested. Fix continuity and source motion before adding decorative effects. See [after-effects-and-qa.md](references/after-effects-and-qa.md).
8. **Deliver honestly.** Distinguish concept, raw generation, preview, final export, collected project and published post. Validate each promised artifact. A shareable ZIP and a local skill are not publicly indexed assets.

## Quality decisions that matter

- A calm subject with fast effects needs real breathing, balance and secondary motion, not a still image with a camera pan.
- Make an impact visible through force direction, torso acceleration, delayed limbs, cloth drag and recovery. Camera shake reinforces an existing event; it does not create missing body mechanics.
- Preserve screen-space momentum through adjacent shots. Front and rear impacts must share an airborne pose and position before force reverses.
- A speed ramp needs a readable approach, brief perceptual anchor and acceleration out. Uniformly speeding a shot removes the movement the user liked.
- Keep effect depth explicit: foreground, contact plane, midground echoes and background atmosphere; vary colour and motion by layer.
- Separate deliberate brief glitch treatment from accidental frame tearing, black gaps, frozen chunks, crop edges and failed interpolation.
- Reuse the original face and footage as compositing sources when identity has drifted. Additional heads must remain the same person if that is the concept.
- A reference request is a request for evidence. Return to the actual reference if successive generations drift; do not keep explaining away mismatches.

## Covers and type

For a matching cover, read [covers-and-references.md](references/covers-and-references.md). Keep generation separate from exact typography: image previews can suggest a type style, while native text uses an available font and explicit spacing. Preserve a wide film when cropping would remove key effects; a separate vertical cover is a distinct artifact.

For a wide film presented inside a vertical Reel, read [reel-presentation.md](references/reel-presentation.md). Establish whether the surrounding treatment is a still optical illusion or an animated surface before adding motion. Approve a still first and preserve the original film and music during layout changes.

## Reusable assets

- [Production brief and shot contract](references/production-template.md): fill only relevant fields.
- [Portable prompt](PROMPT.md): for assistants without skill loading.
- `scripts/verify_media.py`: local ffprobe/ffmpeg inspection and optional ZIP CRC check. Requires Python 3, ffmpeg and ffprobe; it does not generate, upload or change the film.

The workflow adapts to restrained, abstract, performance or psychedelic work. The example aesthetic is not a requirement to add strobes, religious imagery, many arms, black-and-white portraits or a fixed duration to every project.
