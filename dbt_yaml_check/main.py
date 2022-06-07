import json
from operator import itemgetter
from pathlib import Path

import typer
from tabulate import tabulate

app = typer.Typer(add_completion=False)


@app.callback(invoke_without_command=True)
def callback(
    target_dir: Path = typer.Option(
        default="target", exists=True, file_okay=False, dir_okay=True
    )
):
    """
    `dbt-yaml-check` is a utility to check that `dbt` nodes defined in YAML exist in SQL.
    """
    manifest_file = target_dir / "manifest.json"
    catalog_file = target_dir / "catalog.json"

    error_on_exit = False

    table_columns = []

    if manifest_file.exists() and catalog_file.exists():
        manifest = json.load(open(manifest_file))
        catalog = json.load(open(catalog_file))

        manifest_nodes = {
            k.lower(): [c.lower() for c in v["columns"].keys()]
            for k, v in manifest["nodes"].items()
            if v["resource_type"] != "test"
        }

        catalog_nodes = {
            k.lower(): [c.lower() for c in v["columns"].keys()]
            for k, v in catalog["nodes"].items()
        }

        for node in manifest_nodes:
            for column in manifest_nodes[node]:
                if node in catalog_nodes and column not in catalog_nodes[node]:
                    table_columns.append((node.split(".")[-1], column))
                    error_on_exit = True
    else:
        typer.echo(
            f"Could not find manifest.json and catalog.json at {target_dir}, did you run 'dbt docs generate'?"
        )
        error_on_exit = True

    if table_columns:
        typer.secho(
            tabulate(
                sorted(table_columns, key=itemgetter(1, 0)),
                headers=["SQL Node", "Missing Column"],
                tablefmt="pretty",
            ),
            fg=typer.colors.YELLOW,
        )

    if error_on_exit:
        raise typer.Exit(1)


if __name__ == "__main__":
    callback()
