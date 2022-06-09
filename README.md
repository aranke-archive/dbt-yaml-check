# dbt-yaml-check

`dbt-yaml-check` checks that columns defined in YAML also exist in SQL.

This is particularly useful for identifying extraneous columns and typos in column names.

## Installation

`dbt-yaml-check` requires Python version 3.7 or higher.

```shell
pip install dbt-yaml-check
```

## Usage

```shell
$ cd jaffle_shop
$ dbt run
$ dbt docs generate
$ dbt-yaml-check
+-----------+--------------------+-----+------+
|   Model   |       Column       | SQL | YAML |
+-----------+--------------------+-----+------+
| customers | total_order_amount |  ✕  |  ✓   |
+-----------+--------------------+-----+------+
```

## FAQ

### How can I specify a custom target directory?

Use the `target-dir` option like so: `dbt-yaml-check --target-dir <path_to_your_target>`.
