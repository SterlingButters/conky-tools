import os
import pandas as pd

# Replaces (because we want a different update frequency for the emails):
# ${font sans-serif:normal:size=8}Name $alignr PID   CPU%   MEM%${font sans-serif:normal:size=8}
# ${top name 1} $alignr ${top pid 1} ${top cpu 1}% ${top mem 1}%
# ${top name 2} $alignr ${top pid 2} ${top cpu 2}% ${top mem 2}%
# ${top name 3} $alignr ${top pid 3} ${top cpu 3}% ${top mem 3}%
# ${top name 4} $alignr ${top pid 4} ${top cpu 4}% ${top mem 4}%
# ${top name 5} $alignr ${top pid 5} ${top cpu 5}% ${top mem 5}%
# ${top name 6} $alignr ${top pid 6} ${top cpu 6}% ${top mem 6}%
# ${top name 7} $alignr ${top pid 7} ${top cpu 7}% ${top mem 7}%
# ${top name 8} $alignr ${top pid 8} ${top cpu 8}% ${top mem 8}%
# ${top name 9} $alignr ${top pid 9} ${top cpu 9}% ${top mem 9}%
# ${top name 10} $alignr ${top pid 10} ${top cpu 10}% ${top mem 10}%

top = os.popen('top -b -n 1')
s = str(top.read()).split("\n")
# print("\n".join(s[6:15]))

headers = s[6:15][0].split()
table = []
for line in s[6:15][1:]:
    data = line.split()
    table.append((tuple(data)))

df = pd.DataFrame(table, columns=headers)
df = df[['PID', '%CPU', "%MEM", "TIME+", "COMMAND"]]
for i in range(len(df)):
    if float(df.iloc[i]['%CPU']) > 30.0:
        df.iloc[i]['%CPU'] = "${{color red}}{}${{color}}".format(df.iloc[i]['%CPU'])

print(df.to_string(index=False))
