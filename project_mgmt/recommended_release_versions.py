# -*- coding: utf-8 -*-

import click
import re
import json
import requests
import semver
import os


def _exit_with_error(error):
    click.echo("ERROR: {}".format(error))
    sys.exit(1)


def _request(path):
    url = "https://api.github.com/repos/learningequality/kolibri/" + path
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Authorization": "token {}".format(token)} if token else {}
    r = requests.get(url, headers=headers)
    if r.status_code == 403:
        if not token:
            logging.info(
                "You can set a GITHUB_TOKEN environment variable with a github API token.\n"
                + "Generate a github token at https://github.com/settings/tokens and give it read-only permission."
            )
        _exit_with_error("You've hit the Github API rate limit.")
    else:
        r.raise_for_status()
    return r.json()


def _get_versions_from_git_tags():

    ########### SWAP #########
    # response = _request("git/refs/tags")
    with open("./project_mgmt/tags.json") as f:
        response = json.load(f)
    ##########################

    REF = "^refs/tags/v(\d+.\d+.\d+(-\w+)?)$"
    return [
        semver.parse_version_info(re.match(REF, tag["ref"]).group(1))
        for tag in response
        if re.match(REF, tag["ref"])
    ]


def _patch_versions_match(a, b):
    return a.major == b.major and a.minor == b.minor and a.patch == b.patch


def recommended_release_versions(project_page_url):
    # Look for something like:
    # https://www.notion.so/learningequality/Kolibri-0-12-8-is-released-ebad7f3811174cbb9c3a852b2b49c15d
    match = re.search("0-\d+-\d+", project_page_url)
    if not match:
        click.echo("WARNING: No version string found in project URL")
        return []

    # guess which version the notion project refers to
    target = semver.parse_version_info(match.group(0).replace("-", "."))

    # pull tags from git and find the latest pre-release
    existing_versions = _get_versions_from_git_tags()
    latest = max(v for v in existing_versions if _patch_versions_match(v, target))
    if not latest.prerelease:
        click.echo(
            "WARNING: Version {} has already been tagged as final".format(latest)
        )
        return []

    # determine whihc pre-release specifically
    PRERELEASE_PATTERN = "^(\w+)(\d+)$"
    match = re.match(PRERELEASE_PATTERN, latest.prerelease)
    if not match:
        click.echo(
            "WARNING: Unexpected prerelease string in git tag {}".format(
                latest.prerelease
            )
        )
        return []
    prerelease_type, prerelease_number = match.group(1), match.group(2)
    if prerelease_type not in ("alpha", "beta"):
        click.echo(
            "WARNING: Unknown prerelease type in git tag {}".format(latest.prerelease)
        )
        return []

    # suggest a couple reasonable options
    suggested_beta = 0 if prerelease_type == "alpha" else prerelease_number + 1
    suggested_beta = "beta{}".format(suggested_beta)
    return [
        semver.VersionInfo(latest.major, latest.minor, latest.patch, suggested_beta),
        semver.VersionInfo(latest.major, latest.minor, latest.patch),
    ]
