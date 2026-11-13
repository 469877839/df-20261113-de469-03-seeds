# Local evaluation environment
Upstream source: https://github.com/edsu/pymarc/commit/cf33051421ac74389c1bc6d54921fb9612083d1b
Original license: BSD-2-Clause. Original notices remain in this snapshot.
This snapshot adds a pinned dependency list and local environment instructions.
Upstream CI workflows are omitted. Private-key demonstration fixture files are omitted: none.
The PyXLSB synthetic baseline, when present, is newly authored for baseline verification; it contains no task implementation.
The project is an evaluation snapshot, not a submission to upstream. No upstream approval or human review is asserted.

Validated with CPython 3.11.16 on Linux. Use a native Linux checkout for POSIX tests.
```sh
uv venv --python 3.11.16 .venv
export PATH="$PWD/.venv/bin:$PATH"
export PYTHONUTF8=1
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export AWS_EC2_METADATA_DISABLED=true
export SETUPTOOLS_SCM_PRETEND_VERSION=0.0.0+domain
export SERVER=NONE
export VERBOSE=FALSE
mkdir -p .venv/tmp
export TMPDIR="$PWD/.venv/tmp"
uv pip install --python .venv/bin/python -r requirements-domain.lock
.venv/bin/python -B -m pytest -q -o addopts= -p no:cacheprovider test
```
Tests use synthetic data, repository samples, loopback peers or recorded responses.
Reset by checking out this exact commit into a fresh directory and recreating the virtual environment.
For source-only libraries, imports run from the repository root; no system package installation is needed.
