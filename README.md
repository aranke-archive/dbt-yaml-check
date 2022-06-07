# dbt-yaml-check

`dbt-yaml-check` is a utility to check that `dbt` nodes (✅models ✅seeds ❌tests) defined in YAML exist in SQL.

## Installation

`dbt-yaml-check` requires Python version 3.7 or higher.

```shell
pip install dbt-yaml-check
```

## Usage

```shell
$ cd jaffle_shop
$ dbt docs generate --warn-error
$ dbt-yaml-check
+-----------+--------------------+
| SQL Node  |   Missing Column   |
+-----------+--------------------+
| customers | total_order_amount |
+-----------+--------------------+
```

## FAQ

### How can I specify a custom target directory?

Use the `target-dir` option like so: `dbt-yaml-check --target-dir <path_to_your_target>`.
