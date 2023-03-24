#  Copyright (c) 2023 Wh1isper
#  Licensed under the BSD 3-Clause License
#  Created by @Wh1isper 2023/1/4
import sys
from pathlib import Path

import click

from km2testcase.model import convert
from km2testcase.parser import parse_km
from km2testcase.writter import write


@click.command()
@click.argument("markdown_file_path")
@click.option("--output", default=None, help="Output path of converted csv file.")
@click.option(
    "--encoding", default=sys.getdefaultencoding(), help="Output path of converted csv file."
)
@click.option("--details", default=False, help="Print details when converting model")
def cli(markdown_file_path, output, encoding, details, output_type="csv", platform="zentao"):
    markdown_path = Path(markdown_file_path)
    if not output:
        suffix = output_type.lstrip(".")
        output = markdown_path.with_suffix("." + suffix)
    else:
        output = Path(output)
    case_models = parse_km(markdown_path, encoding=encoding, echo=details)
    print(f"{len(case_models)} testcases parsed.")
    if not case_models:
        print("No testcase found, exiting...")
        return

    write(
        [convert(case_model, platform, echo=details) for case_model in case_models],
        output,
        output_type,
        encoding=encoding,
    )


if __name__ == "__main__":
    import os

    _here = os.path.dirname(__file__)
    cli([os.path.join(_here, "../EXAMPLE.km"), "--details", "True"])
