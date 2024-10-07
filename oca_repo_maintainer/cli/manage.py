# Copyright 2023 Dixmit
# @author: Enric Tobella
# Copyright 2023 Camptocamp SA
# @author: Simone Orsi
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import click

from ..tools.conf_file_manager import ConfFileManager
from ..tools.manager import RepoManager


@click.command()
@click.option("--conf-dir", required=True, help="Folder where configuration is stored")
@click.option(
    "--token", required=True, prompt="Your github token", envvar="GITHUB_TOKEN"
)
@click.option(
    "--org",
    default="OCA",
    prompt="Your organization",
    help="The organizattion.",
)
def manage(conf_dir, org, token):
    """Setup and update repositories and teams."""
    RepoManager(conf_dir, org, token).run()


@click.command()
@click.option("--conf-dir", required=True, help="Folder where configuration is stored")
@click.option("--branch", required=True, help="New branch name to add")
@click.option(
    "--default/--no-default", default=True, help="Set default branch as default."
)
def add_branch(conf_dir, branch, default=True):
    """Add a branch to all repositories in the configuration."""
    ConfFileManager(conf_dir).add_branch(branch, default=default)


if __name__ == "__main__":
    manage()
