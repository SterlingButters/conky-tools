import os
import json

sensors = os.popen('sensors -f -j')
out_list = json.loads(str(sensors.read()))

print(json.dumps(out_list, indent=4))


