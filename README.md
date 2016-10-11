# FonetiPy


FonetiPy implements the BuscaBR algorithm in Python to match misspelled or ambiguous words at Brazil. It's fully inspired at [Ruby Fonetica](https://github.com/sobrinho/fonetica)

## Install:

Install via PIP tool:

```python
pip install fonetipy
```

## Usage:

A simple usage is:

```python
from fonetipy import FonetiPy

search = FonetiPy()

search('wagner batista')  # show "VM BT"
search('vagner baptista')  # show "VM BT"
```

You can also use a shortcut `fonetipy`

```python
from fonetipy import fonetipy

fonetipy('Wagner batista')  # show "VM BT"
fonetipy('Vagner baptista')  # show "VM BT"
```

## Tests:

Just run:

```python fonetipy_test.py```

The verbose mode is active by default.

