"""Save verified manual review batches from the local translation workspace."""
import argparse
import collections
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parent.parent
TOKENS = re.compile(r"\{[^{}]*\}|\[(?:[^\[\]]|\[[^\[\]]*\])*\]")
CHARACTERS = ("alexis", "audrey", "bree", "sasha", "harems_full", "_ac", "_bg", "_da", "_ev", "_root")

def read(path):
    return json.loads(path.read_text(encoding="utf-8"))
def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review-root", required=True, type=Path)
    parser.add_argument("--remaining-limit", required=True, type=int)
    args = parser.parse_args()
    central = args.review_root.resolve()
    assert 0 <= args.remaining_limit <= 100
    snapshot = read(ROOT / "provenance/snapshot.json")
    # Do not bless unrelated changes while updating saved draft files.
    for name, digest in snapshot["files"].items():
        assert sha(ROOT / name) == digest, ("unrecorded modification", name)
    groups = {}
    updated = set()
    for girl in CHARACTERS:
        if not any((central / "receipts").glob(girl + "_*.json")):
            continue
        data = read(central / "data" / (girl + "_existing.json"))
        rows = data["rows"]
        seen = set()
        edits = {}
        excluded = []
        receipts = []
        for receipt_path in sorted((central / "receipts").glob(girl + "_*.json")):
            receipt = read(receipt_path)
            start, end = receipt["reviewed_range"]
            assert receipt["end_exclusive"] and 0 <= start < end <= len(rows)
            assert not seen.intersection(range(start, end))
            seen.update(range(start, end))
            skipped = receipt.get("not_approved_for_retranslation", [])
            excluded.extend(skipped)
            batch = read(central / "batches" / receipt_path.name)
            for key, target in batch.items():
                index = int(key)
                assert start <= index < end and index not in skipped and key not in edits
                assert isinstance(target, str) and target.strip() and "\ufffd" not in target
                assert target != rows[index]["existing"]
                assert collections.Counter(TOKENS.findall(rows[index]["source"])) == collections.Counter(TOKENS.findall(target)), (girl, index)
                edits[key] = target
            receipts.append(receipt_path)
        assert seen == set(range(max(seen) + 1))
        installed = sum(int(i) < 3000 for i in edits) if girl == "alexis" else 0
        groups[girl] = dict(reviewed=len(seen), total=len(rows), corrections=len(edits),
                            installed_corrections=installed, pending_corrections=len(edits) - installed,
                            excluded_from_retranslation=sorted(excluded))
        for receipt_path in receipts:
            for folder in ("batches", "receipts"):
                target = ROOT / "work-in-progress/review" / folder / receipt_path.name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(central / folder / receipt_path.name, target)
                updated.add(target.relative_to(ROOT).as_posix())
        target = ROOT / "work-in-progress/review" / (girl + "_edited_context.json")
        write(target, {i: rows[int(i)] for i in sorted(edits, key=int)})
        updated.add(target.relative_to(ROOT).as_posix())
    candidate_root = central.parent / "finalreview_20261020"
    if not (candidate_root / "release_validation.json").exists():
        candidate_root = central.parent / "allreview_20261020"
    if not (candidate_root / "release_validation.json").exists():
        candidate_root = central.parent / "fullreview_20261020"
    if not (candidate_root / "release_validation.json").exists():
        candidate_root = central.parent / "ownreview_20261020"
    frozen = read(candidate_root / "data/frozen.json")["groups"]
    final_candidate = candidate_root.name.startswith("finalreview_")
    candidate_label = "combined01" if final_candidate else "candidate02" if candidate_root.name.startswith("allreview_") else "candidate01"
    candidate_report = candidate_root / "results" / candidate_label / "validation.json"
    candidate_status = read(candidate_report)["status"] if candidate_report.exists() else "running"
    release_report = candidate_root / "release_validation.json"
    release_status = "incomplete"
    if release_report.exists():
        report = read(release_report)
        assert report["status"] == "passed_with_scope"
        assert len(report["evidence"]) == (7 if final_candidate else 5)
        if final_candidate:
            assert "fragments01/fragments-validation.json" in report["evidence"]
            assert "coverage01/coverage.json" in report["evidence"]
        for name, evidence in report["evidence"].items():
            source = release_report.parent / "results" / name
            assert evidence["status"] == read(source)["status"] == "passed"
            assert sha(source) == evidence["sha256"]
        target = ROOT / "work-in-progress/isolated-validation.json"
        write(target, report)
        updated.add(target.relative_to(ROOT).as_posix())
        if final_candidate:
            exports = {
                "candidate/lssb_localization_ru/allreview_manifest.json": "manifest.json",
                "results/combined01/validation.json": "native-validation.json",
                "results/fragments01/fragments-validation.json": "fragments-validation.json",
                "results/coverage01/coverage.json": "coverage.json",
                "visual_review.json": "visual-review.json",
                "fragments-expected.json": "fragments-expected.json",
                "ui-remaining.json": "ui-strings.json",
                "archive-readback.json": "archive-readback.json",
                "queue-closure.json": "queue-closure.json",
                "latin-review.json": "latin-review.json",
            }
            for source_name, name in exports.items():
                target = ROOT / "work-in-progress/finalreview" / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(candidate_root / source_name, target)
                updated.add(target.relative_to(ROOT).as_posix())
        if candidate_root.name.startswith(("fullreview_", "allreview_")):
            prefix = candidate_root.name.split("_")[0]
            exports = {
                f"compile/lssb_localization_ru/game/zz_lssb_{prefix}_ru.rpy": f"zz_lssb_{prefix}_ru.rpy",
                f"candidate/lssb_localization_ru/{prefix}_manifest.json": "manifest.json",
                f"results/{candidate_label}/validation.json": "native-validation.json",
                "visual_review.json": "visual-review.json",
            }
            for source_name, name in exports.items():
                target = ROOT / "work-in-progress" / prefix / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(candidate_root / source_name, target)
                updated.add(target.relative_to(ROOT).as_posix())
        release_status = "passed isolated native, UI and disable/enable checks; not installed; no full playthrough"
    active = next((girl for girl in CHARACTERS
                   if girl in groups and groups[girl]["reviewed"] < groups[girl]["total"]), None)
    progress = dict(updated_utc=datetime.now(timezone.utc).isoformat(), active_character=active,
                    groups=groups, remaining_limit_at_checkpoint=args.remaining_limit,
                    stop_at_remaining_percent=7, shutdown=False, wiki_translation=False,
                    installed_versions=dict(localization="1.79.0", manager="1.2.76"),
                    isolated_candidate=dict(profile="own-mods-only", alexis_corrections=frozen["alexis"]["corrected"],
                                            workspace=candidate_root.name,
                                            corrections=sum(g["corrected"] for g in frozen.values()),
                                            groups=frozen,
                                            audrey_reviewed=frozen["audrey"]["reviewed"],
                                            audrey_corrections=frozen["audrey"]["corrected"],
                                            native_check=candidate_status,
                                            status=release_status))
    target = ROOT / "work-in-progress/PROGRESS.json"
    if final_candidate:
        progress["isolated_candidate"].update(
            corrections=report["unique_changed_statements"],
            versions=report["versions"],
            dynamic_statements=24,display_strings=44,random_phrases=15,
            native_say_coverage=report["native_say_coverage"],
            sources_in_mods=True)
    write(target, progress)
    updated.add(target.relative_to(ROOT).as_posix())
    for name in updated:
        snapshot["files"][name] = sha(ROOT / name)
    write(ROOT / "provenance/snapshot.json", snapshot)
    handoff = central.parent / "handoff"
    write(handoff / "ACTIVE_REVIEW.json", progress)
    latest = read(handoff / "LATEST_STATE.json")
    latest["updated_utc"] = progress["updated_utc"]
    latest["draft"] = dict(character=active, groups=groups, installed=False, path=str(central),
                           status="review_in_progress" if active else "sources_built_and_validated_not_installed" if final_candidate else "known_existing_text_queues_complete")
    if final_candidate:
        latest["prepared_release"] = dict(path=str(candidate_root), versions=report["versions"],
                                          installed=False, status=report["status"])
    latest.pop("additional_pending", None)
    latest["active_review"] = str(handoff / "ACTIVE_REVIEW.json")
    write(handoff / "LATEST_STATE.json", latest)
    print(json.dumps(groups, ensure_ascii=False))

if __name__ == "__main__":
    main()
