# rdkbmesh-zap

## Description

**rdkbmesh-zap** is a python-based plugin repo of zaero framework targetted to test RDKB Mesh Nodes.

---

## Prerequisites

Make sure you have the following installed:

* zaero package - https://github.com/zilogic-systems/zaero

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/zilogic-systems/rdkbmesh-zap.git
```

### 2. Generate .whl file

```
cd rdkbmesh-zap
python3 -m build
```

### 3. Install rdkbmeshzap Package

```
cd dist/
python3 -m pip install rdkbmeshzap-<version>-py3-none-any.whl
```

---

## Usage

### Run Test Cases

```
cd test/
python3 -m pytest --log-cli-level=INFO <test_file>.py -v -s
```

---

## Author

Zilogic Systems