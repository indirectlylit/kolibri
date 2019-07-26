# -*- coding: utf-8 -*-
import click
import questionary
import os
import sys
from notion.client import NotionClient
from recommended_release_versions import recommended_release_versions


def _exit_with_error(error):
    click.echo("ERROR: {}".format(error))
    sys.exit(1)


def _determine_target_version(project_url):
    version_options = recommended_release_versions(project_url)
    choices = []
    for v in version_options:
        title = str(v) if v.prerelease else "{} (RC and final)".format(v)
        choices.append(questionary.Choice(title, str(v)))
    choices.append("Other")
    target_version = questionary.select(
        "What release are we planning?", choices=choices
    ).ask()
    if target_version == "Other":
        target_version = questionary.text("Enter target release").ask()
    return target_version


@click.command()
def main():
    """Generate a Notion release checklist in Notion"""

    token = os.environ.get("NOTION_TOKEN")
    if not token:
        click.echo("No NOTION_TOKEN environment variable set. You can enter it here.")
        token = questionary.password("Notion token_v2\n").ask()

    click.echo("Initializating connection with Notion...")
    client = NotionClient(token, monitor=False)

    project_url = questionary.text("Notion project URL\n").ask()

    if not project_url.startswith("https://www.notion.so/learningequality/"):
        _exit_with_error("Project must be an LE notion.so URL")

    target_version = _determine_target_version(project_url)

    print(target_version)

    _collection_id = "ddac0397-7d24-427c-8402-39a07a6c7110"
    collection = client.get_collection(_collection_id)


    # project_page = client.get_block(project_url)
    # click.echo("DONE!")


if __name__ == "__main__":
    main()
