#!/usr/bin/env python3
"""Compare rebuilt pages with the published reference; uses only Python's stdlib."""

from html.parser import HTMLParser
from pathlib import Path
import hashlib
import json
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / ".hugo-build"
VOID = set("area base br col embed hr img input link meta param source track wbr".split())


class Element:
    def __init__(self, tag="document", attrs=()):
        self.tag, self.attrs, self.children = tag, dict(attrs), []

    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child, Element):
                yield from child.walk()

    def text(self):
        if self.tag in {"script", "style"}:
            return ""
        return " ".join(c.text() if isinstance(c, Element) else c for c in self.children)

    def has_class(self, name):
        return name in self.attrs.get("class", "").split()


class Document(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.root = Element()
        self.stack = [self.root]
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        element = Element(tag, attrs)
        self.stack[-1].children.append(element)
        if tag not in VOID:
            self.stack.append(element)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def primary(document, homepage=False):
    nodes = list(document.root.walk())
    predicates = (
        [lambda n: n.tag == "body"] if homepage else [
            lambda n: n.attrs.get("id") == "profile-page",
            lambda n: n.tag == "article",
            lambda n: n.has_class("pub"),
            lambda n: n.has_class("universal-wrapper"),
            lambda n: n.tag == "body",
        ]
    )
    for predicate in predicates:
        for node in nodes:
            if predicate(node):
                return node
    return document.root


def text(node):
    return re.sub(r"\s+", " ", node.text()).strip()


def digest(path):
    return hashlib.sha256(path.read_bytes()).digest()


def main():
    tracked = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
    routes = [p for p in tracked if p.endswith(".html") and not p.startswith(("js/", "hugo/"))]
    errors = []
    for route in routes:
        target = BUILD / route
        if not target.is_file():
            errors.append(f"Missing route: {route}")
            continue
        before, after = Document(ROOT / route), Document(target)
        if text(primary(before, route == "index.html")) != text(primary(after, route == "index.html")):
            errors.append(f"Published content differs: {route}")

    # Every local image, script, stylesheet, PDF, and generated page link must resolve.
    for path in BUILD.rglob("*.html"):
        if path.relative_to(BUILD).parts[0] == "js":
            continue  # The vendored slide presenter is not a site page.
        for node in Document(path).root.walk():
            for attribute in ("href", "src"):
                url = urlsplit(node.attrs.get(attribute) or "")
                if url.scheme or url.netloc or not url.path:
                    continue
                local = unquote(url.path)
                destination = BUILD / local.lstrip("/") if local.startswith("/") else path.parent / local
                if not destination.exists() and not (destination / "index.html").exists():
                    errors.append(f"Broken link in {path.relative_to(BUILD)}: {local}")

    reference_index = json.loads((ROOT / "index.json").read_text())
    generated_index = json.loads((BUILD / "index.json").read_text())
    expected = {(p["relpermalink"], p["title"]) for p in reference_index}
    actual = {(p["relpermalink"], p["title"]) for p in generated_index}
    if expected != actual:
        errors.append("Search index has different pages or titles")
    if digest(ROOT / "files/cv.pdf") != digest(BUILD / "files/cv.pdf"):
        errors.append("Built CV differs from the updated published CV")
    if (BUILD / "CNAME").read_bytes() != (ROOT / "CNAME").read_bytes():
        errors.append("Custom domain changed")
    if errors:
        raise SystemExit("\n".join(sorted(set(errors))))
    print(f"Verified {len(routes)} published routes and their primary content, local links, search index, CV, and custom domain.")


if __name__ == "__main__":
    main()
