"""Dry-run-first job manifest builder; no provider calls or image generation."""
import argparse
import json
from pathlib import Path

def make_manifest(job_id: str):
    return {"job_id":job_id,"status":"pending","phases":[{"name":"illustration","status":"pending","requires":["character_references","scene_prompt"]},{"name":"typesetting","status":"pending","requires":["verbatim_textscript","illustration"]},{"name":"audit","status":"pending","checks":["gutter","face_clearance","speech_tails","text_verbatim","prose_breathing_room"]}]}

def main():
    p=argparse.ArgumentParser(); p.add_argument("job_id"); p.add_argument("--output",type=Path); args=p.parse_args()
    data=json.dumps(make_manifest(args.job_id),indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(data+"\n")
    else: print(data)
if __name__=="__main__": main()
