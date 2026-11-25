# After Effects refinement and delivery

## Target the live project deliberately

Verify the open project path and intended composition before changing anything. A connected AE tool may target an unrelated project. Preserve approved edits and music. Keep one working project with short review exports; do not delete all old media to reduce UI clutter or memory use.

If a local macOS workflow uses AppleScript, some installations respond to `DoScript` evaluating a JSX file even when `DoScriptFile` fails. Treat this as a tested fallback, not a universal API guarantee. Use bounded calls and a status file written by the JSX; an AppleScript return value alone does not prove the work succeeded. If a call times out, inspect its status and application state before resubmitting.

Avoid global key presses against uncertain focus. Use document APIs or narrowly targeted app control. Do not change machine-wide approval hooks, security settings or unrelated application configuration as an automatic part of film editing.

## Composite with spatial attachment

- **Eye light:** track iris/eyelid geometry; mask and occlude emitters behind eyelids and glasses. Build a small hot core, detailed iris texture, rings with staggered expansion and local light spill. A large untracked orb usually reads as a sticker.
- **Chest correction:** identify the exact malformed area and affected frame interval. Track a motivated light/energy element over that area, matching perspective, luminance, occlusion and the original effect direction. Fade it before the next pattern takes over. Do not hide the entire torso for the whole shot.
- **Layer depth:** vary scale, parallax, sharpness, opacity and temporal phase. Keep one visual hierarchy; every layer need not peak simultaneously.
- **Impact:** attach local distortion to the contact region; add a short directional camera kick with decay, motion blur and edge coverage. Review shake on the actual musical accent.
- **Glitch:** use deliberate short channel displacement, exposure or temporal accents. Reject unintended horizontal seams, repeated chunks, missing frames and crop gaps. A request for glitches is not permission to retain render defects.
- **Camera/crop:** allow sufficient image overscan for shake and transforms. Preview the complete frame at maximum displacement. Add cinematic bars after the picture transformations when that matches the intended presentation.

Use available native effects first when they achieve the look. For stock elements inspect the actual account entitlement and final asset: an application subscription does not prove a particular stock asset is licensed. Watermarked previews stay out of final delivery.

## Review by defect, then by sequence

Name the symptom, targeted interval and acceptance criterion: e.g. "eye approach reads before entry", "shoe detail briefly anchors the ramp", "head motion is legible", "hand hold ends before momentum dies", "front and rear impulses share the same airborne state". Review source motion and retiming before adding effects. Show the short section if requested, then check its surrounding transitions in the full film.

## Render and verify

1. Save the correct composition and confirm frame rate, start/end frame, duration and audio routing.
2. Render to a local temporary location when a cloud-synced target causes partial writes. Validate before atomically replacing the delivery export.
3. Probe codecs, dimensions, frame count, duration and audio. Decode the whole file. Detect black intervals, but review whether any detected black is intentional.
4. Inspect representative frames and actual playback, especially optical-flow warps, crop edges, impact contact, titles and final frame. Confirm music alignment and listen; audio-stream presence alone is insufficient.
5. For a collected project, include all dependencies of the delivery comps, including relevant disabled layers. Reduce a COPY of the project, relink into its Media folder, reopen the original WIP afterwards.
6. Move the collected folder and reopen its project to test portability. Audit that every required file resolves inside the relocated package, not back into the original workspace; simply reopening without a missing-media warning is insufficient. Record any missing fonts/plugins. Test ZIP CRC and verify its promised file list. Do not call a source package portable if relocation and resolved paths were not checked.

The supplied verification script performs technical checks, not aesthetic review, licensing review, frame-exact musical judgment or live-AE portability verification. Report those separately.
