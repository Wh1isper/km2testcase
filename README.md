![](https://img.shields.io/github/license/wh1isper/km2testcase)
![](https://img.shields.io/github/v/release/wh1isper/km2testcase)
![](https://img.shields.io/pypi/dm/km2testcase)
![](https://img.shields.io/github/last-commit/wh1isper/km2testcase)
![](https://img.shields.io/pypi/pyversions/km2testcase)

# Install

`pip install km2testcase`

# Usage

`km2testcase --help`

```
Usage: km2testcase [OPTIONS] MARKDOWN_FILE_PATH

Options:
  --output TEXT      Output path of converted csv file.
  --details BOOLEAN  Print details when converting model
  --help             Show this message and exit.
```

## Hello world

Using [EXAMPLE.km](EXAMPLE.km)

```
km2testcase EXAMPLE.km --details true
```

## Advance config

### Zentao

Given that kity minder does not provide more labels, the type and stage of the use case use environment
variables `ZENTAO_CASE_TYPE` and `ZENTAO_STAGE`

# Develop

Install pre-commit before commit

```
pip install pre-commit
pre-commit install
```

Install package locally

```
pip install -e .[test]
```

Run unit-test before PR, **ensure that new features are covered by unit tests**

```
pytest -v
```

# Practice

Using [vscode-mindmap extension](https://marketplace.visualstudio.com/items?itemName=Souche.vscode-mindmap) on vscode

or Using [DesktopNaotu](https://github.com/NaoTu/DesktopNaotu) locally

or Using Web: https://naotu.baidu.com/

![1678242422431](image/README/1678242422431.png)

# Why Kity Minder(Why not XMind)

- XMind is commercial software, [Kity Minder](https://github.com/fex-team/kityminder) is open-resource
- XMind's performance is poor when there are many cases
- Difficulty in versioning binary files using XMind

# Thanks

Inspired by:

- [xmind2testcase](https://github.com/zhuifengshen/xmind2testcase)

Based on:

- [Kity Minder](https://github.com/fex-team/kityminder)
