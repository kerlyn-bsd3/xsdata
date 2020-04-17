import os
from pathlib import Path

from click.testing import CliRunner

from tests import load_class
from tests import validate_bindings
from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


def test_integration():

    schema = Path("tests/fixtures/defxmlschema/chapter17/chapter17.xsd")
    package = "tests.fixtures.defxmlschema.chapter17"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Order")
    validate_bindings(schema, clazz)


def test_example1713():
    schema = "tests/fixtures/defxmlschema/chapter17/example1713.xsd"
    package = "tests.fixtures.defxmlschema.chapter17"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
