# CatBase
JSON-based database you were dreaming of!

## Quickstart

```py
from catbase import CatDB

db = CatDB("example.json")

db["test"] = "apple"
print(db["test"])

db.commit() # commit to save changes
```

## Features

### Autocommiting
```py
from catbase import CatDB

db = CatDB("example.json", autocommit=True)

db["test"] = "apple" # CatDB commits here automatically!
print(db["test"])
# no commit required!
```

### KeyError safety
```py
from catbase import CatDB

db = CatDB("example.json")

# oh no! "test" doesnt exist yet!
print(db["test"])
# output: None
```

### Custom KeyError defaults
```py
from catbase import CatDB

db = CatDB("example.json", none = 3)

# oh no! "test" doesnt exist yet again!
print(db["test"] + 1)
# output: 4
```

### Broken JSON safety
```py
from catbase import CatDB

db = CatDB("example.json", safe = False)

# now, if the example.json is corrupt, db will be empty instead of crashing.
# safe is set to True by default.
```
