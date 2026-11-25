#!/usr/bin/env python3
"""Inspect a film without modifying it. Python stdlib + ffmpeg/ffprobe."""
import argparse
import json
import math
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path


def run(args):
    return subprocess.run(args, capture_output=True, text=True, timeout=600)


def inspect(video, expected=None, require_audio=False, archive=None):
    report = {"video": str(video), "errors": [], "warnings": [], "checks": {}}
    for binary in ("ffmpeg", "ffprobe"):
        if not shutil.which(binary):
            report["errors"].append(f"Required executable unavailable: {binary}")
    if report["errors"]:
        return report
    probe = run(["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(video)])
    if probe.returncode:
        report["errors"].append("Probe failed: " + probe.stderr.strip())
        return report
    data = json.loads(probe.stdout)
    report["probe"] = data
    streams = data.get("streams", [])
    vids = [s for s in streams if s.get("codec_type") == "video"]
    auds = [s for s in streams if s.get("codec_type") == "audio"]
    if not vids:
        report["errors"].append("No video stream")
    if require_audio and not auds:
        report["errors"].append("Required audio stream is absent")
    def duration_of(obj):
        try:
            value = float(obj.get("duration"))
            return value if math.isfinite(value) and value >= 0 else None
        except (TypeError, ValueError):
            return None
    container_duration = duration_of(data.get("format", {}))
    video_duration = duration_of(vids[0]) if vids else None
    report["durations"] = {"container": container_duration, "primary_video": video_duration}
    if expected is not None:
        if not math.isfinite(expected) or expected <= 0:
            report["errors"].append("Expected duration must be finite and positive")
        elif video_duration is None:
            report["errors"].append("Expected video duration cannot be verified: primary video duration unavailable")
        else:
            for label, duration in (("primary video", video_duration), ("container", container_duration)):
                if duration is not None and abs(duration - expected) > 0.1:
                    report["errors"].append(f"Duration of {label} {duration:.3f}s differs from expected {expected:.3f}s")
    if video_duration is None or container_duration is None:
        report["warnings"].append("One or more duration fields unavailable or non-finite")
    decode = run(["ffmpeg", "-v", "error", "-xerror", "-i", str(video), "-map", "0:v?", "-map", "0:a?", "-f", "null", "-"])
    report["checks"]["full_decode"] = decode.returncode == 0
    if decode.returncode:
        report["errors"].append("Full decode failed: " + decode.stderr.strip())
    if vids:
        black = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(video), "-map", "0:v:0", "-vf", "blackdetect=d=0.05:pix_th=0.05", "-an", "-f", "null", "-"])
        intervals = re.findall(r"black_start:([\d.]+) black_end:([\d.]+) black_duration:([\d.]+)", black.stderr)
        report["black_intervals"] = [{"start": float(a), "end": float(b), "duration": float(c)} for a, b, c in intervals]
        if black.returncode:
            report["errors"].append("Black-interval analysis failed: " + black.stderr.strip())
        elif intervals:
            report["warnings"].append("Review detected black intervals against intentional edits")
    if auds:
        loud = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(video), "-map", "0:a:0", "-vn", "-af", "loudnorm=I=-14:TP=-1:LRA=11:print_format=json", "-f", "null", "-"])
        match = re.search(r'\{\s*"input_i".*?\}', loud.stderr, re.S)
        if loud.returncode or not match:
            report["errors"].append("Audio loudness analysis failed")
        else:
            report["audio_loudness_analysis"] = json.loads(match.group())
            report["warnings"].append("Audio presence and loudness do not establish content, audibility or sync; listen")
    if archive is not None:
        try:
            with zipfile.ZipFile(archive) as z:
                bad = z.testzip()
                report["archive"] = {"path": str(archive), "files": z.namelist(), "crc_ok": bad is None}
                if bad:
                    report["errors"].append("ZIP CRC failed: " + bad)
        except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
            report["errors"].append("ZIP check failed: " + str(exc))
    report["warnings"].append("Visual quality, beat alignment and editable-project portability require separate review")
    return report


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("video", type=Path)
    p.add_argument("--expected-duration", type=float)
    p.add_argument("--require-audio", action="store_true")
    p.add_argument("--zip", type=Path, dest="archive")
    p.add_argument("--report", type=Path)
    args = p.parse_args()
    if args.expected_duration is not None and (not math.isfinite(args.expected_duration) or args.expected_duration <= 0):
        p.error("--expected-duration must be finite and positive")
    if args.report and args.report.resolve() in {args.video.resolve(), args.archive.resolve() if args.archive else None}:
        p.error("Report path must not overwrite an input")
    try:
        result = inspect(args.video, args.expected_duration, args.require_audio, args.archive)
    except (OSError, subprocess.TimeoutExpired, json.JSONDecodeError) as exc:
        result = {"video": str(args.video), "errors": [str(exc)], "warnings": [], "checks": {}}
    result["technical_pass"] = not result["errors"]
    output = json.dumps(result, indent=2)
    if args.report:
        args.report.write_text(output + "\n", encoding="utf-8")
    print(output)
    return 0 if result["technical_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
