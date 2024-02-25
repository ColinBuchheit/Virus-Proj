# this file is infected
print("This file is infected")
exec("import zlib\nimport base64\nexec(zlib.decompress(base64.urlsafe_b64decode(b'eNoDAAAAAAE=')))")

import random

random.seed()

for _ in range(10):
  print (random.randint(0,100))
