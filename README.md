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

Given that vscode-mindmap does not provide more labels, the type and stage of the use case use environment
variables `ZENTAO_CASE_TYPE` and `ZENTAO_STAGE`

# Develop

Install pre-commit before commit:

```
pip install pre-commit
pre-commit install
```

Install package locally

```
pip install -e ./
```

**Compatibility with more platforms or additional test cases are currently in demand**

# Practice

Using [vscode-mindmap extension](https://marketplace.visualstudio.com/items?itemName=Souche.vscode-mindmap) on vscode

![1678242422431](image/README/1678242422431.png)

# Why vscode-mindmap(Why not XMind)

- XMind is commercial software, [vscode-mindmap](https://github.com/souche/vscode-mindmap) is open-resource
- XMind's performance is poor when there are many cases
- Difficulty in versioning binary files using XMind

# Thanks

Inspired by [xmind2testcase](https://github.com/zhuifengshen/xmind2testcase)

pip install -e ./
