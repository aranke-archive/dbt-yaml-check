from typer.testing import CliRunner

from dbt_yaml_check.main import app

runner = CliRunner()

expected = '''
+-----------+--------------------+-----+------+
|   Model   |       Column       | SQL | YAML |
+-----------+--------------------+-----+------+
| customers | total_order_amount |  ✕  |  ✓   |
+-----------+--------------------+-----+------+
'''


def test_jaffle_shop():
    result = runner.invoke(app, ["--target-dir", "tests/jaffle_shop"])
    assert result.exit_code == 1
    assert result.stdout.strip() == expected.strip()
