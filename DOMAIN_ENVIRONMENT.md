# Local evaluation environment
Upstream source: https://github.com/h5netcdf/h5netcdf/commit/8914c0abcb87b02c27c0e08e8db5f9a036f91820
Original license: BSD-3-Clause. Original notices remain in this snapshot.
This snapshot adds a pinned dependency list and local environment instructions.
Upstream CI workflows are omitted. Private-key demonstration fixture files are omitted: none.
The PyXLSB synthetic baseline, when present, is newly authored for baseline verification; it contains no task implementation.
The project is an evaluation snapshot, not a submission to upstream. No upstream approval or human review is asserted.

Validated with CPython 3.13.15 on Linux. Use a native Linux checkout for POSIX tests.
```sh
uv venv --python 3.13.15 .venv
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
uv pip install --python .venv/bin/python --no-build-isolation --no-deps -e .
.venv/bin/python -B -m pytest -q -o addopts= -p no:cacheprovider -k 'not test_is_classic' h5netcdf/tests/test_h5netcdf.py
```
Tests use synthetic data, repository samples, loopback peers or recorded responses.
Reset by checking out this exact commit into a fresh directory and recreating the virtual environment.
For source-only libraries, imports run from the repository root; no system package installation is needed.
