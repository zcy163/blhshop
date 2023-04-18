from django.test import TestCase

# Create your tests here.
from urllib.parse import urlencode, quote
import json
import string

param = {
    "offset": 33444
}
print()

print(quote(json.dumps(param).replace(" ", "")))
