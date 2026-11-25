# Wide film inside a vertical Reel

Use this when a cinematic film should remain wide while the surrounding vertical canvas becomes part of the design. It is optional presentation guidance, not a default style for every film.

## Separate picture, surface and typography

Keep the approved film as its own nested composition. Remove only verified letterbox pixels; do not crop active picture to fit a tall format. Measure the bars on representative frames rather than assuming a fixed height. Centre the active picture and retain its timing and soundtrack.

Use a separate surface behind the film and native editable text above it. Preserve the approved words, font, word spacing and placement. Check readability at phone size, and verify the current platform's interface before relying on a fixed safe area.

If a generated layout mockup includes a movie still and typography, isolate only its decorative background for production. Replace the mockup's picture and lettering with the actual film and native text. Feather background masks without exposing fragments of the generated picture or headline. Render and inspect the real composition; the mockup does not prove the final layout works.

## Physical depth can be static

Ask what the requested illusion means through the user's reference and feedback. "Make the whole phone screen feel carved" may mean a fixed material illusion, not flowing curves or beat pulses.

For the engraved-black treatment developed in this workflow:

- Use a few broad curved recesses with gradual changes in depth and width. Fine dense lines can read as decorative texture at small size.
- Place soft grazing highlights consistently along upper bevels and darker occlusion inside the recesses. Broader shading makes depth legible without increasing overall brightness.
- Keep most of the surface near black. Use restrained colour on selected edges that relates to the film's palette.
- Blend the carving gradually into solid black at the perimeter and near the movie. Keep the headline over a quiet region.
- Preserve a clear boundary between movie and surrounding surface unless the user explicitly requests effects spilling across it.
- Compare one still against the approved version before changing the full film. Avoid swinging from an excessively bright pattern to an almost invisible one.

If the static treatment is approved, keep transforms, lights and opacity fixed throughout the export. If animation is requested separately, test restrained lighting on fixed geometry first. Moving the surface is a different creative decision.

## Verify and hand off

Inspect opening, climax and ending at phone size, including edge fades and title placement. For a static surround, compare the background regions at separated times in a lossless render; allow for tiny output-dithering differences rather than mistaking them for motion. Do not include moving film pixels in that comparison.

Keep the approved soundtrack aligned. If copying it directly into an export, compare audio bitstream hashes; otherwise compare decoded audio and listen. Verify duration, frame count, dimensions and full decode as described in [after-effects-and-qa.md](after-effects-and-qa.md).

For a requested social-sharing ZIP, include only the selected final Reel, cover and profile image. Verify the ZIP and compare each entry with its intended source. An editable source package is a separate deliverable unless requested. Keep one current working project and make the latest deliverable unambiguous.
