import os
import pandas as pd

tracked_services = ['v4l2-kinect', 'tailscaled', 'x11vnc', 'windscribe-cli']

awk = [" || /{}.service/".format(service) for service in tracked_services]
awk = "".join(awk)

out = os.popen("systemctl list-units -a | awk 'NR<=1 {}'".format(awk))
out_list = str(out.read()).split("\n")[:-1]
table = []
for l in range(len(out_list)):
    if l>0:
        split_line = out_list[l].split()
        if split_line[0] == "●":
            new_line = split_line[:5]+[" ".join(split_line[6:])]
        else:
            new_line = [""]+split_line[:4]+[" ".join(split_line[5:])]

        table.append((new_line))

df = pd.DataFrame(table, columns=[" "]+out_list[0].split())
print(df.to_string(index=False))

print("\n",
"""LOAD   = Reflects whether the unit definition was properly loaded.
 ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
 SUB    = The low-level unit activation state, values depend on unit type.""")

