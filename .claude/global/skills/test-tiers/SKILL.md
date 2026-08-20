---
name: test-tiers
description: Derive which subset of the test suite to run for a change, in layers (touched-area only → +conformance → full suite), instead of always running everything. Use when about to run tests during or at the end of a task, especially in repos with large (500+) test suites. Args (optional) select the tier: "1", "2", "3", or a description of the change.
---

# test-tiers — run the narrowest test layer that covers the change

Large suites are cheap to run green (a filtering hook keeps passing-test output out of
context — see the `lean-test` skill), but they are not free: latency scales with test count,
and any failure ingests a traceback. Running 1500+ tests to validate a two-file change wastes
both. Run tests in tiers, narrowest first, and only escalate when the tier's job requires it.

## The three tiers

- **Tier 1 — during the task.** Only the test paths that plausibly cover the files just
  changed. Fast feedback loop while iterating.
- **Tier 2 — closing the task.** Tier 1's paths **plus** the project's architectural/contract
  gate (conformance suite, layer-import checks, lint-as-test, etc.) if the project has one —
  never skip this even for a one-line change, since it catches boundary violations Tier 1
  won't.
- **Tier 3 — sprint/delivery gate only.** The full suite, once, run through the project's
  economical runner (e.g. `lean-test`) if one exists, otherwise plain `pytest -q` /
  `npm test` / equivalent. Not run per-task — only at a real milestone boundary (PR ready,
  sprint close), on a high-blast-radius change (shared core/contracts/infra), or when
  explicitly asked for a full regression pass.

If the project defines its own closing gate (e.g. a `guardrails-check` skill with a
regression floor), that gate decides when Tier 3 runs — keep the two consistent: the
per-task close is Tier 2; the full-suite regression floor belongs to milestone gates and
high-blast-radius changes, not to every task.

## How to derive the Tier 1/2 subset

1. Get the changed files: `git diff --name-only` (or `git diff --name-only <base>...HEAD` for
   a branch's full diff).
2. Check for a project-specific mapping first — if `CLAUDE.md` or a project doc defines an
   area→tests table (e.g. "touched `screenwriter` → `tests/regression/integration_screenwriter`"),
   use it verbatim; it encodes knowledge a generic heuristic can't.
3. Otherwise, derive by convention, in order of confidence:
   - Same-name test file: `src/foo/bar.py` changed → look for `tests/**/test_bar.py` or
     `tests/**/bar/`.
   - Shared directory segment: a change under `.../<area>/...` → any test path containing
     `<area>` as a directory segment.
   - Import/reference search: if naming doesn't match, Grep the test tree for the changed
     module's import path or class/function names to find tests that exercise it.
4. Always append the project's fast structural/architectural gate to the Tier 2 command if one
   exists (conformance tests, contract tests, lint) — these are cheap and catch a different
   class of bug than the feature tests.
5. If no confident subset can be derived (e.g. a change to shared core/infra code with wide
   fan-out, or a new file with no obvious test home), fall back to the full suite filtered
   through the economical runner — don't guess narrowly on high-blast-radius changes.

## Running it

Reuse whatever the project already provides for filtered output — do not add a second
pipe/filter on top of an existing one. If the project has a `lean-test` (or similarly named)
skill, pass the derived path(s) to it: `/lean-test tests/regression/integration_screenwriter -x`.
Otherwise run the test command directly with the narrowed path.

## Reporting

State which tier ran and why (e.g. "Tier 1: narrowed to `tests/foo/` based on the diff"), the
result (pass count / failures), and — if something failed — enough of the traceback to act on,
not the full log.
