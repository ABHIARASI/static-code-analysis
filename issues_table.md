# Issues Found and Fixes

| Issue Type | Tool | Line(s) | Description | Fix |
|-------------|------|---------|--------------|-----|
| Mutable default argument | Pylint | addItem | Function used `logs=[]` as a default argument, causing shared data across calls | Changed default to `logs=None` and initialized inside the function |
| Bare except | Pylint / Bandit | removeItem | Used `except:` which hides real errors | Replaced with specific exceptions (`KeyError`) and added logging |
| Use of eval() | Bandit | main | `eval()` can execute arbitrary code, creating a security risk | Removed `eval()` call |
| File not closed properly | Pylint | loadData, saveData | Files opened manually using `open()` but not closed safely | Used `with open(...) as f:` context manager |
| Missing input validation | Pylint | addItem | Function accepted any type of argument | Added type checks for `item` (str) and `qty` (int) |
