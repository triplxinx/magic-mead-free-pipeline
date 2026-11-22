# Magic Mead image and archive import plan

The cross-project asset discovery inventory is maintained in [magic-mead-production](https://github.com/triplxinx/magic-mead-production/blob/main/docs/DISCOVERED_ASSET_INVENTORY.md).

## Rules
- Keep canonical art and approved final spreads in magic-mead-production; keep only minimal licensed fixtures and pipeline test renders here.
- Extract images from ZIP/PDF/HTML and documents **before** choosing which files belong in Git.
- Preserve source filename, archive entry path, SHA-256, original revision, author and canonical/draft/alternate status.
- Do not push unpublished manuscripts, secrets, raw third-party reference photos or other restricted content to a public repo without review.
- GitHub blocks individual normal Git files larger than 100 MiB; use appropriate Git LFS or release storage for large approved assets.
- Never commit binary data as text or imply that the discovery inventory itself is an asset upload.

## Remaining work
- [ ] Complete paginated Library discovery
- [ ] Materialize and inspect all archives and documents
- [ ] Extract embedded images and deduplicate by SHA-256
- [ ] Confirm rights and public-release classification
- [ ] Publish eligible binary assets and link them in a verified manifest
- [ ] Test pipeline image loading and canonical reference mapping
