import os
import pandas as pd

out = os.popen('do-release-upgrade -c')
print(str(out.read()))

pip = os.popen('pip list --outdated')
out_list = str(pip.read()).split("\n")

table = []
for l in range(len(out_list)):
    if l > 1:
        table.append((out_list[l].split()))

df = pd.DataFrame(table, columns=out_list[0].split())

print(df.to_string(index=False))

out = os.popen('apt list --upgradeable')
out_list = str(out.read()).split("\n")

print(out_list)

# table = []
# for l in range(len(out_list)):
#     if l > 1:
#         table.append((out_list[l].split()))
#
# df = pd.DataFrame(table, columns=out_list[0].split())
#
# print(df.to_string(index=False))

