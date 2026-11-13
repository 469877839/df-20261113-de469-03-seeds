# Local evaluation environment
Upstream source: https://github.com/pymodbus-dev/pymodbus/commit/7509a6b204e5c8a1cf9f67f4acf5e1c8db400017
Original license: BSD-3-Clause. Original notices remain in this snapshot.
This snapshot adds a pinned dependency list and local environment instructions.
Upstream CI workflows are omitted. Private-key demonstration fixture files are omitted: examples/certificates/pymodbus_tls.key.
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
.venv/bin/python -B -m pytest -q -o addopts= -p no:cacheprovider -k 'test_register_read_requests or test_register_read_responses or test_register_read_response_decode or test_datastore_server or test_tcp_framer_transaction or test_client_mixin_convert_fail or test_client_mixin_convert_1234' -p pytest_asyncio.plugin -p pytest_timeout --timeout=8 test/framer/test_extras.py test/pdu/test_register_read_messages.py test/datastore/test_context.py test/client/test_client.py
```
Tests use synthetic data, repository samples, loopback peers or recorded responses.
Reset by checking out this exact commit into a fresh directory and recreating the virtual environment.
For source-only libraries, imports run from the repository root; no system package installation is needed.
