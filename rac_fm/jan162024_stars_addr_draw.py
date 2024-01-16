# Draw 1 address from all the addresses.
# Each address has the same chance of winning.

import numpy as np

list_of_wallets = [
    'stars10a29hu7chl55ar4wsyjueqxc7smudpvrjlh53k',
    'stars1v5ft27rre0m3th7etfvm5c8vhw462vh672yd66',
    'stars1vcjyhwzpa60g9ht6v37xyjw8wqgjmh0v3vw06adw6krd5pckuk8s3x4nv9',
    'stars1hmda69ykt8rzsrxanrxm2r837edln3pjmzmtdr',
    'stars1k5c9pg9l9v7jfjthlzf6zuxw2hs3yw44e2jgnl',
    'stars13mzcw7ezlgzcgpls7xqxpsg5qqsxvp8je5fehz',
    'stars1rxakrn8x4gwc6wcrpttpz8htjfu43nswn7363l',
    'stars137p2qrs3qw00c28679pwu4a76md48q8zv75rv9',
    'stars1ev7ev8zersa49z2q25smw4v34jggm269l9may0',
    'stars1k4wzk63hdcr33s59jzpqs7kz66r5p45e4q8yrf',
    'stars1w93f099t4pp9jamyghp88p60fvkg39dx92tufd',
    'stars1jvm8gy4lgzcrsagxpyhvvxymz982y3j58xg6sr',
    'stars1xhwcv9egw7qgx8ef7v032tk2fga58ayupvtv2y',
    'stars1tkgyd0c0pjdxcu6f7z4h8g65whvdcsqhlhwguj',
    'stars19njf667kw2acwfpapupm5z4tfckfjyy9gn8ynd',
    'stars1japufgdf82gtm0rxq3y3aasq905d4ek5lquaud',
    'stars1s2tnan9yrc7mhrywvhdx76g7hu9szd3l2vw33j',
    'stars1jmpqtl6msvelzuyw83maq05wrnw3jdfz3s3acg',
    'stars1xuwl7x8htyl26t7pe3l0x6auj3j9jwd2k26qx5',
    'stars1jzt962czzt3ruwsapec9fzmrm7kcj442vjk36c',
    'stars1624d37zzhx0p4de4rk6r32nf2sfysrzhv6k29f',
    'stars1uaq57q70pxu4vmn0jzsnmcr7pkazaecyes89gz',
    'stars1yfgvyv3jxact4l6vkdfs0kdtsfvkd0ch8rd5tl'
]

# Seed has been taken from random.org: 530742272 ->
# 706141545
# Min: 1, Max: 999999999
# 2024-01-16 18:09:31 UTC

seed = 706141545
np.random.seed(seed)

print(f"Drawing from {len(list_of_wallets)} addresses...")

winners = np.random.choice(list_of_wallets, 1, False)

for idx, winner in enumerate(winners):
    print(f"Winner #{idx+1} -> {winner}")
print(f"Congrats :D")

# Drawing from 23 addresses...
# Winner #1 -> stars1jmpqtl6msvelzuyw83maq05wrnw3jdfz3s3acg
# Congrats :D