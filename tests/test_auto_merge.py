import os
import subprocess
import unittest
from pathlib import Path

import yaml

WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/dependabot-auto-merge.yml"


class AutoMergeTest(unittest.TestCase):
    def test_only_patch_and_minor_reach_approval_and_merge(self):
        steps = yaml.safe_load(WORKFLOW.read_text())["jobs"]["auto-merge"]["steps"]
        script = next(
            step["run"] for step in steps if step["name"] == "Approve and enable auto-merge"
        )
        pr = "https://example.invalid/pull/1"
        cases = {
            "version-update:semver-patch": True,
            "version-update:semver-minor": True,
            "version-update:semver-major": False,
            "": False,
            "version-update:unrecognized": False,
        }
        for update_type, eligible in cases.items():
            with self.subTest(update_type=update_type):
                result = subprocess.run(
                    ["bash", "-c", 'gh() { echo "$1 $2 $3"; }\n' + script],
                    env={
                        "PATH": os.defpath,
                        "UPDATE_TYPE": update_type,
                        "DEPENDENCY_NAMES": "example",
                        "GITHUB_STEP_SUMMARY": os.devnull,
                        "APPROVE": "true",
                        "MERGE_METHOD": "squash",
                        "PR_URL": pr,
                    },
                    check=True,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(
                    result.stdout.splitlines(),
                    ["pr review --approve", "pr merge --auto"] if eligible else [],
                )


if __name__ == "__main__":
    unittest.main()
