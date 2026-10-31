# local-gate

Throwaway repository for the Orbi engine promotion gate (local self-hosted mode).
Created by `~/orbi-deploy/e2e-scripts/local_gate.py`; one repository per gate run.

## Usage

Run the snippet below from the repository root (Python >= 3.11, no extra
dependencies):

```python
from app import greet

print(greet("Ada"))
```

Output:

```text
Hello, Ada
```

`greet(name)` returns `Hello, <name>`; an empty or `None` name returns
`Hello, stranger`.
