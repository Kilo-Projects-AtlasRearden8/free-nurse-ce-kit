#!/usr/bin/env python3
"""Validation for the Free Nurse CE Kit (Asdale Dynamics, LLC)."""
import html.parser
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(ROOT)
failures = []


def fail(msg):
    failures.append(msg)
    print("FAIL: " + msg)


class TagChecker(html.parser.HTMLParser):
    """Very light structural sanity check: tags close, no stray doctype issues."""

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.stack = []
        self.void = {
            "area", "base", "br", "col", "embed", "hr", "img", "input",
            "link", "meta", "param", "source", "track", "wbr",
        }

    def handle_starttag(self, tag, attrs):
        if tag not in self.void:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.void:
            return
        if not self.stack:
            fail(f"{self.name}: closing </{tag}> with no open tag")
            return
        if self.stack[-1] != tag:
            fail(f"{self.name}: expected </{self.stack.pop()}> before </{tag}>")
        else:
            self.stack.pop()

    def finish(self):
        for tag in self.stack:
            fail(f"{self.name}: unclosed <{tag}>")


def check_html(path):
    print("checking " + os.path.relpath(path, PROJECT))
    with open(path, encoding="utf-8") as f:
        content = f.read()
    if "<!DOCTYPE html>" not in content[:200]:
        fail(path + ": missing doctype")
    parser = TagChecker(os.path.basename(path))
    parser.feed(content)
    parser.finish()
    # Required kit markers
    for marker in ["Asdale Dynamics, LLC", "Education only", "no-print", "@media print"]:
        if marker not in content:
            fail(path + ": missing marker '" + marker + "'")
    if '<meta charset="utf-8">' not in content:
        fail(path + ": missing utf-8 charset")
    if not re.search(r'<h1[^>]*>', content):
        fail(path + ": missing h1 title")
    # inputs/selects should have the fill class (fillable)
    inputs = re.findall(r'<\s*(?:input|select|textarea)\b[^>]*>', content)
    for m in inputs:
        if "class=\"fill\"" not in m and "class='fill'" not in m:
            fail(path + ": non-fillable form control: " + m[:90])
    return content


def check_exact_file(path, expected, label):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    if expected not in content:
        fail(path + ": missing " + label + " line: " + expected)


def check_secrets(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    patterns = {
        "api key": r"(?i)(api[_-]?key|secret[_-]?key|access[_-]?token)\s*[:=]\s*['\"]?[A-Za-z0-9_-]{16,}",
        "password": r"(?i)(password|passwd)\s*[:=]\s*['\"]?[^\s'\"]{6,}",
        "private key": r"-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----",
    }
    for label, pat in patterns.items():
        for m in re.finditer(pat, content):
            fail(path + ": possible secret (" + label + "): " + m.group(0)[:80])


def main():
    html_files = [
        "ce-tracker.html",
        "license-renewal-calendar.html",
        "course-log.html",
        "reflection-templates.html",
    ]
    md_files = [
        "ce-tracker.md",
        "license-renewal-calendar.md",
        "course-log.md",
        "reflection-templates.md",
    ]
    for f in html_files:
        check_html(os.path.join(PROJECT, f))
    for f in md_files:
        p = os.path.join(PROJECT, f)
        if not os.path.exists(p):
            fail("missing " + f)
        else:
            check_secrets(p)
    for f in html_files + ["assets/style.css"]:
        check_secrets(os.path.join(PROJECT, f))

    # LICENSE exact copyright line
    lic = os.path.join(PROJECT, "LICENSE")
    check_exact_file(lic, "Copyright (c) 2026 Asdale Dynamics, LLC", "LICENSE copyright")

    # README credit + copyright line
    readme = os.path.join(PROJECT, "README.md")
    with open(readme, encoding="utf-8") as f:
        rc = f.read()
    for phrase in ["Asdale Dynamics, LLC", "Copyright (c) 2026 Asdale Dynamics, LLC", "MIT License"]:
        if phrase not in rc:
            fail("README.md missing phrase: " + phrase)

    # No .github/workflows
    wf = os.path.join(PROJECT, ".github", "workflows")
    if os.path.exists(wf):
        fail(".github/workflows exists (must not)")

    print("\n" + ("=" * 60))
    if failures:
        print("VALIDATION FAILED — %d issue(s):" % len(failures))
        for m in failures:
            print(" - " + m)
        return 1
    print("VALIDATION PASSED — all HTML, LICENSE, README, and secret checks OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
