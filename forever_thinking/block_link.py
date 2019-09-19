import hashlib
import json

block_1 = {'prev_hash':None, 'transactions':[1, 3, 4, 2]}
block_1_fuck = json.dumps(block_1, sort_keys=True).encode('utf-8')
block_1_hash = hashlib.sha256(block_1_fuck).hexdigest()

block_2 = {'prev_hash':block_1_hash, 'transactions':[2, 4, 6, 8]}
block_2_fuck = json.dumps(block_2, sort_keys=True).encode('utf-8')
block_2_hash = hashlib.sha256(block_2_fuck).hexdigest()
print(block_2_hash)