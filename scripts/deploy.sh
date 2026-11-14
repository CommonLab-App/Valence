#!/usr/bin/env sh
# Builds and copies dist/ to the host. The target (user@host:path) lives in .env as VALENCE_DEPLOY, never in the repo.
set -eu
cd "$(dirname "$0")/.."
. ./.env
npm run build
# .well-known/ and cgi-bin/ are the host's own (certificate checks); never deleted here.
# --no-perms: folders already on the host, the web root among them, keep the permissions the host gave them.
rsync -az --delete --no-perms --chmod=D755,F644 --exclude .well-known/ --exclude cgi-bin/ dist/ "$VALENCE_DEPLOY/"
