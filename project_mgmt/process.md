"""

A
# 0.12.6 - update changelog

B[A]
# 0.12.6 RC (beta 3) - github release

C[B]
# 0.12.6 RC (beta 3) - PyPi publish
## Reference
- [https://kolibri-dev.readthedocs.io/en/develop/release_process.html#publish-to-pypi](https://kolibri-dev.readthedocs.io/en/develop/release_process.html#publish-to-pypi)
## Checklist
- [ ]  Get build file from buildkite
- [ ]  Test locally
- [ ]  run `make release` and publish final release to PyPi using credentials or private key

D[C]
# 0.12.6 RC (beta 3) - sanity check pip package
    check multiple OSes, multiple versions of Python

E[D]
# 0.12.6 final - github release
## Reference
- [https://kolibri-dev.readthedocs.io/en/develop/release_process.html#create-the-final-release](https://kolibri-dev.readthedocs.io/en/develop/release_process.html#create-the-final-release)
## Checklist
- [ ]  Update __init__.py version file to 0.12.6 final VERSION = (0, 12, 6, "final")
- [ ]  Create a final release using Github's Releases page (creates a v0.12.6 tag)
- [ ]  Copy the contents of the changelog into the release notes
- [ ]  Build the .pex and sanity check that it runs
- [ ]  Delete any previous v0.12 beta releases (on GH Releases page)
- [ ]  Update __init__.py version file to 0.12.7 beta: VERSION = (0, 12, 7, 'beta', 0)
- [ ]  Create a v0.12.7-alpha0 tag. Can be done by creating and then deleting a github release.
- [ ]  Merge release-v0.12.x into develop, resolving inevitable conflict with version file. Develop should be at 0.13.0 alpha. DO NOT USE GITHUB's WEB-BASED MERGE UI

F[E]
# 0.12.6 final - PyPi publish
## Reference
- [https://kolibri-dev.readthedocs.io/en/develop/release_process.html#publish-to-pypi](https://kolibri-dev.readthedocs.io/en/develop/release_process.html#publish-to-pypi)
## Checklist
- [ ]  Get build file from buildkite
- [ ]  Test locally
- [ ]  run `make release` and publish final release to PyPi using credentials or private key

G[E]
# 0.12.6 - close milestone
If it's not open yet, create 0.12.7 milestone


H[E]
# 0.12.6 final - update demo server

I[F]
# 0.12.6 final - generate/test/sign Windows

J[F]
# 0.12.6 final - generate/test/sign Debian

K[F]
# 0.12.6 final - generate/test/sign Android

L[I,J]
# 0.12.6 - packages available for download
- [ ]  Upload Windows, Debian, and .pex packages to Google Cloud Storage
- [ ]  Update website variables to point at new packages
- [ ]  Set blog URL to empty string
- [ ]  Make sure all download links on website work

M[L,E]
# 0.12.6 - communications published
- [ ]  Publish post on Medium
- [ ]  Update website variables to point to new blog post
- [ ]  Send newsletter
- [ ]  Send newsletter
- [ ]  Tweet announcement


Others:
# 0.12.6 - Triage open issues
# 0.12.6 - Send update notification



