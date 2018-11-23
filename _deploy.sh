#!/bin/sh

set -e

[ -z "${GITHUB_PAT}" ] && exit 0
[ "${TRAVIS_BRANCH}" != "master" ] && exit 0

git config --global user.email "eroualdes@csuchico.edu"
git config --global user.name "Edward A. Roualdes"

git clone -b gh-pages https://${GITHUB_PAT}@github.com/${TRAVIS_REPO_SLUG}.git doc-output
cd doc-output
cp -r ../doc/build/html/* ./
git add --all *
git commit -m"Update the docs" || true
git push -v origin gh-pages
