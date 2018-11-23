#!/bin/sh

set -e

[ -z "${GITHUB_PAT}" ] && exit 0
[ "${TRAVIS_BRANCH}" != "master" ] && exit 0

git clone -b master https://${GITHUB_PAT}@github.com/${TRAVIS_REPO_SLUG}.git doc-output
cd doc-output
cp -r doc/build/html/* ./
git add --all *
git commit -m"Update the docs" || true
git push -q origin gh-pages
