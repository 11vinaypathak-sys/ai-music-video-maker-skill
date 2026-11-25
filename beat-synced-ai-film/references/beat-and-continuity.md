# Beat mapping and continuity

## Establish a reliable musical clock

Use a local audio file or an authorized accessible source. A video URL, song name or BPM estimate alone does not establish beat timestamps. If audio cannot be retrieved, say what is missing and work provisionally without inventing timing.

Probe duration and sample rate, listen to the proposed excerpt, inspect waveform transients, and use onset/tempo tools only as candidates. Confirm the audible drop, accented subdivisions, pauses and actual ending by listening. A detected onset may be a vocal consonant rather than a musical accent. Preserve the original audio throughout picture refinements.

Keep a compact marker table:

```csv
time_seconds,kind,confidence,edit_intent
0.000,excerpt_start,confirmed,calm opening
3.200,accent,provisional,head response candidate
```

These values are illustrative. Record the source excerpt offset separately. Convert to timeline frames with the actual project frame rate and retain source seconds; half/double-tempo ambiguity and rounding can otherwise shift later edits.

## Cut density is not shot count

One continuous shot can carry several accents: a camera acceleration, iris pulse, 2-frame colour separation, occlusion wipe and a new layer appearing. Reserve actual cuts for useful changes in angle or narrative. Avoid a predictable new generated image on every beat.

For each transition record:

| Property | Outgoing state | Incoming constraint |
|---|---|---|
| Identity | Hair, glasses, face, clothes | Same anchors unless intentionally changing |
| Pose | Head angle, spine, limbs, airborne height | Match the handoff pose |
| Motion | Screen direction, speed, angular motion | Continue it or show the cause of reversal |
| Camera | Position, focal length feel, angle, horizon | Match or motivate the move |
| Lighting | Key direction, exposure, effect colours | No unexplained jump |
| Effects | Origin, velocity, age, density | Carry their momentum into the next state |

Use a real final frame from the approved take as a continuation reference when supported. A similar standalone picture is not necessarily a match frame.

## Retiming

Map source time to timeline time explicitly. A typical fast/slow/fast passage reveals the detail briefly before accelerating to the next beat; actual hold duration depends on the shot. Maintain monotonically advancing source time except for an intentional reversal. Avoid duplicating frames for long holds when hair, clothing or effects should remain alive.

Inspect interpolation on glasses, fingers, silhouette edges and layered effects. Optical flow may produce more visible defects than a shorter cut. Do not change audio speed to repair picture timing unless explicitly requested.

Review sections with neighbouring shots, not only in isolation. A polished eye close-up can still fail if the approach or exit has incompatible camera momentum.
