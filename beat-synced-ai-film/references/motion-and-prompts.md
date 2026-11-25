# Motion design and generation contracts

## Separate four motion systems

| System | Specify |
|---|---|
| Body | Initial pose, action amplitude, acceleration, delayed limbs, recovery, expression |
| Camera | Start angle, trajectory, speed changes, focal-length behaviour, endpoint |
| Effects | Origin, propagation, layer velocities, interaction, occlusion, dissipation |
| Edit | Beat accents, hold/ramp windows, flashes, shake decay, transition boundary |

Do not ask a video model to infer all four from phrases such as "more cinematic", "gravity", "crazy" or "trippy". Translate those adjectives into observable events. Keep a shot's causal chain short enough for its available duration. If generation cannot reliably perform the whole chain, split at a motivated occlusion or match frame and make the split explicit.

## Example: rear impact to expansive reveal

This is a project-derived example, not a default shot for every film.

1. Continue the exact existing airborne pose, screen position and camera angle.
2. Trails previously travelling past the subject curve behind the back. Separate layers visibly converge and compress into one tiny bright point behind the upper torso.
3. That point releases a sudden rear impulse. The torso accelerates away from contact; neck, forearms and knees lag, clothing follows with inertia. Preserve a calm face. There is no visible fist or attacker.
4. At contact, begin the rapid camera pullback. Let the initial body reaction read before settling into a brief suspended pose. The subject becomes nearly still while cloth and energy continue moving.
5. The same person's enlarged refracted silhouettes emerge from the body one after another. Face, arm and atmospheric layers have distinct phase offsets and velocities. The effect's size is revealed by camera movement and parallax.
6. Let the force and camera vibration decay into the agreed next-shot handoff. Avoid returning abruptly to a standing pose.

An illustrative six-second allocation might place convergence in the first second, contact/pullback immediately after, expansion across the middle, and recovery at the end. Anchor the real timings to the chosen music and approved edit; do not reuse those numbers blindly.

## Copyable motion-prompt structure

```text
CONTINUITY: Continue from [approved frame/take], preserving [identity anchors],
[clothing], [airborne/standing pose], [screen position], [camera angle], [scene].
SHOT: One continuous [duration] shot. [Event A] causes [B], which triggers [C].
BODY: [Small natural performance], then [force direction + torso response],
with delayed [limbs/cloth] and [recovery]. Expression remains [description].
CAMERA: [Start], [trajectory], [contact-timed acceleration], [end framing].
EFFECTS: [Origin + material], [compression/expansion path], [layer velocities],
[occlusion/parallax], [colour roles], [dissipation]. Effects keep moving during
the brief body suspension.
HANDOFF: End with [exact pose, motion direction, exposure and visual state].
OUTPUT: [Provider-supported duration/resolution/audio setting].
AVOID: [Relevant observed defects only: identity drift, deep head bow,
static stacked images, unrelated dance, rigid body, detached overlay].
```

Use UI/API settings for silence, aspect ratio, resolution and model selection when available; text alone is not a reliable settings override. Record returned output attributes and listen/check the audio stream.

## Credit-aware iteration

Maintain a ledger with attempt ID, provider, exact model/version, parameters, quoted units, submitted job ID, charged units if verified, status and approval scope. Provider credits are separate currencies: never add them into one pooled total without identifying the units. Distinguish quotes from confirmed charges and unknown charge states.

An authorized one-take cap means one submission within that cap, not unlimited retries below a per-take price. A premium comparison is a new decision when it exceeds the existing authorization. Review raw source quality before trying to hide a failed generation under editing effects.

Reuse a proven model and seed/reference strategy where available. Do not silently switch models because a tool endpoint is easier to access. A small proof can use lower resolution if the user accepts that tradeoff; final upscaling cannot guarantee recovery of lost identity or motion detail.
