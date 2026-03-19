#!/usr/bin/env python3
import hashlib, json, os, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "day5"
SCHEMA_VERSION = "5.0"

def now_utc(): return datetime.now(timezone.utc).isoformat()
def token_hash8(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()[:8]

def sha256_file(p: Path) -> str:
    if not p.exists(): return ""
    return hashlib.sha256(p.read_bytes()).hexdigest()

def read_json(p: Path):
    if not p.exists(): return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except: return {}

def contains_text(p: Path, needle: str) -> bool:
    if not p.exists(): return False
    return needle in p.read_text(encoding="utf-8", errors="replace")

def main() -> int:
    token = os.getenv("STUDENT_TOKEN", "").strip()
    name = os.getenv("STUDENT_NAME", "").strip()
    group = os.getenv("STUDENT_GROUP", "").strip()
    th8 = token_hash8(token) if token else "no_token"

    p_yang_tree = ART / "yang" / "pyang_tree.txt"
    yang_ok = contains_text(p_yang_tree, "+--rw interfaces")

    p_webex_room = ART / "webex" / "room_create.json"
    room_data = read_json(p_webex_room)
    room_title = room_data.get("title", "")
    webex_ok = th8 in room_title if th8 != "no_token" else False

    p_pt_ext = ART / "pt" / "external_access_check.json"
    p_pt_dev = ART / "pt" / "network_devices.json"
    p_pt_hosts = ART / "pt" / "hosts.json"
    
    pt_ext_data = read_json(p_pt_ext)
    pt_dev_data = read_json(p_pt_dev)
    pt_hosts_data = read_json(p_pt_hosts)

    empty_ticket_seen = "empty ticket" in str(pt_ext_data).lower()
    version_ok = pt_dev_data.get("version") == "1.0" and pt_hosts_data.get("version") == "1.0"
    pt_ok = empty_ticket_seen and version_ok

    summary = {
        "schema_version": SCHEMA_VERSION,
        "generated_utc": now_utc(),
        "student": {"token": token, "token_hash8": th8, "name": name, "group": group},
        "yang": {
            "ok": yang_ok,
            "evidence_sha": sha256_file(p_yang_tree)
        },
        "webex": {
            "ok": webex_ok,
            "room_title_contains_hash8": webex_ok,
            "evidence_sha": sha256_file(p_webex_room)
        },
        "pt": {
            "ok": pt_ok,
            "empty_ticket_seen": empty_ticket_seen,
            "evidence_sha": sha256_file(p_pt_dev)
        },
        "validation_passed": bool(yang_ok and webex_ok and pt_ok),
        "run": {"python": sys.version.split()[0], "platform": sys.platform}
    }

    out = ART / "summary.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")
    
    print(f"Summary generated at {out}")
    return 0 if summary["validation_passed"] else 2

if __name__ == "__main__":
    sys.exit(main())