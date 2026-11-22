# Magic Mead Free Pipeline — History and requirements
## About
Free-tier-oriented, local-first production automation for **MAGIC MEAD & THE POLITICAL DEATH MACHINE**, coordinating reference-conditioned illustration, deterministic lettering/typesetting and independent audits. The pipeline must never rewrite approved dialogue and must stop for human review at chapter milestones. Distinct from the creative canon repository.

## Revision history
- 2026-11-09: Requested NotebookLM chapter-by-chapter slide/prompt packs and a three-phase workflow; asked for reference sheets and no-cost, slower alternatives.
- 2026-11-12: Requested automated seven-chapter packs, five-spread batches, two-page spread output, illustration prompt → typesetting prompt → non-image audit, populated filesystem.
- 2026-11-12: Requested multiple free-tier GPU/image backends with reference support and optional final image-to-image style homogenization.
- 2026-11-12–15: Requested hands-off third-phase fit checks, chapter-level review pauses, prompt audits, source reconciliation, and Kaggle single-account walkthrough.
- 2026-11-15: Requested a single-source setup/control UI for credentials, safety guidance, starting and monitoring engines.
- 2026-11-15–16: Requested two online-only free pipelines, automatic pause/resume, per-chapter approval, and up to 14 friends/accounts with independently authorized logins, fair scheduling and available Colab/Kaggle resources.
- 2026-11-16: Pipeline folder specification: book/, pipeline.py, requirements.txt, requirements-art.txt, workers/, shared/, Free-GPU-Colab.ipynb, START-HERE.md; command example `python pipeline.py run --job SP_010_011 --offload`.
- 2026-11-16: Reported Blend OS immutable Arch/Pillow installation error; asked for reproducible dependency installation without modifying immutable host.
- 2026-11-16: Checkpoint history references MM-192-v12, 192 pages, 97 jobs, 185 panel directions, 861 lettering entries, 7 clocks and specific pilot order; verify against approved source before production.

## Feature inventory
- [ ] Read-only approved imagescript.txt/textscript.txt, SHA-256 source manifests and immutable reference assets.
- [ ] Per-chapter prompt packs for all seven chapters, spread IDs and multi-job queues.
- [ ] Reference-conditioned illustrations with canonical character sizes, eyes, tattoos, smoke cloud, wet-acrylic neon style and architecture/landmark accuracy.
- [ ] Two equal 3:4 portrait pages, center gutter protection, aged-paper left page, full/stacked-panel right page.
- [ ] Deterministic lettering using verbatim dialogue/captions; elliptical balloons, smooth outlines, tails to correct speakers; split spreads when text crowded; no page numbers.
- [ ] Automated third-phase checks for gutter, face/hand/balloon overlap, speech-tail assignment, typography, breathing room and text equality; independent human review.
- [ ] Pluggable Colab/Kaggle/local providers with opt-in account authentication, quota and rate-limit handling; never evade provider limits or share account credentials.
- [ ] Pause/resume, crash recovery, durable queue, per-chapter approval gates, revisions, hashes, artifacts and logs.
- [ ] Pilot order SP_010_011 → SP_028_029 → SP_030_031 → SP_008_009 and explicit approval pause before PAGE_001, subject to source validation.
- [ ] Single control dashboard for safe key setup, dependency checks, GPU availability, job launch and monitoring.
- [ ] Optional post-render homogenization with rights-aware reference conditioning; avoid silent drift.
- [ ] Chapter header wheat-paste-flyer brick-wall artwork and consistent day/night style packs.

## Verified current repository
Python CLI emits a three-phase pending job manifest; unit test present. It does not render, typeset, inspect images, schedule GPU jobs or run a production queue.
## Related prior artifacts
Earlier README/Colab notebooks reportedly describe a local-first MVP with read-only scripts, planning, PNG/JSON audit outputs and T4 workflows. They are not assumed to be present here until imported and tested.

## TODO
1. [ ] Audit existing book-generatorish, majikalbrewski, manuscript checkpoint, Colab notebooks and source archives; map reusable code and provenance.
2. [ ] Implement job IDs, validated schemas, immutable script/reference imports and checkpoint persistence.
3. [ ] Integrate actual renderer adapters using user-authorized providers, without pretending mock output is rendered art.
4. [ ] Build deterministic lettering and visual audit engine with objective pass/fail metrics.
5. [ ] Implement approved pilot jobs, retries, chapter pauses, human review UI and audit logs.
6. [ ] Add free-tier resource management, secure credentials and reproducible Colab/Kaggle notebooks.
7. [ ] Validate against approved canon, 192→200-page reconciliation and production checkpoint before batch run.
8. [ ] Add CI, unit/integration tests and explicit verified changelog entries.

## Historical integrity
Accessible prompt reconstruction only; historical claims and checkpoint counts need source verification.
