# Draw 1 address from all the addresses

import numpy as np

list_of_wallets = [
    "omniflix1ssfrydv7qs6qfnx28q7kmkuvuyea724l6v6gka",
    "omniflix1me9w2pu4sf5uad8nfajmck5jmdty8h4crhheg0",
    "omniflix1697eu6zsqnghmac28a2d30y3ffxehpztyue6y7",
    "omniflix10a29hu7chl55ar4wsyjueqxc7smudpvrma3sde",
    "omniflix1xuwl7x8htyl26t7pe3l0x6auj3j9jwd2lguy6m",
    "omniflix1ctq6esla3d299l3768g8329uxghpry2mly0k2j",
    "omniflix13d20nkk96w9qtewmcdm92fzdxzpu0nsnqkwvnq",
    "omniflix1yrql9mf6kfjzlsukwyg0jv7kwaenn78ahdes0c",
    "omniflix1nk9pnpwqy7xa2krmmxls0phdc7xqynmg96f7k3",
    "omniflix1v5ft27rre0m3th7etfvm5c8vhw462vh6hgzfx4",
    "omniflix1v7n4naqgeutqayhr6kvkd7s2pfgapel78tx3qy",
    "omniflix1x6gvw82e27x6jkxmh8jlelmj4gn6mwlp9reqk3",
    "omniflix12uyd20vahq7aqarplvcd20j0lfn4vyjh27hp9g",
    "omniflix14sq8fgpf2f7j9l3w2f8sud26td5ycdnuk37qnw",
    "omniflix1lt9m0faxam9rqghqtxlhrguwev0psyprcyzngr",
    "omniflix10rh584tpl9q7a8utzsmf06eyrwa4a6373aveqc",
    "omniflix13mzcw7ezlgzcgpls7xqxpsg5qqsxvp8jsk0atd",
    "omniflix1u7xwld7jrsj3dh8a7chezj8nj2ac36e8s9fr2n",
    "omniflix1cnwp99x5m24ucfjkh8csn0nt86x4j0vjkdrpv8",
    "omniflix1yvjzddtyg5jt2vruea0wgyqae9dwqy3drd8t4p",
    "omniflix1p9tghhqr2fnzcx8c08rhnsdrwrnqu32hhfjskt",
    "omniflix190v7e0ptl54cv72p55hl6xg490nuyg8nw897q3",
    "omniflix1fkl53tuhq2gf4qa2aghaqhcj7zkflnf7tzcmf8",
    "omniflix1flhs29gr32y3xywvxuzqxymu5pgvyyatxpjaau",
    "omniflix18rr4nz73zvqemcredzrwflw8v25alexnkzyr5h",
    "omniflix1j0ke63m2zu76fgpcacucte2kuckn7xph3my8pr",
    "omniflix1vc4pwx4r58469lk80d3j9uazmsmfval6xnwjy4",
    "omniflix1kv5n4rpxnz7xhpenge8mmg3eawapf7d4sv3mzt",
    "omniflix1pl7ggevu93s5j46qk7wt3fyz6jclf35xpa2mdm",
    "omniflix1d8xtuav36xg7hp6lv6u69gexpd8sunaet4nql9",
    "omniflix1z3rehqm4j4clnjls8gut4eprgd9ep0t6dp8a5h",
    "omniflix1alsed0s9hy2vtuet4dt7wewp5clee8cwrvsjmv",
    "omniflix137p2qrs3qw00c28679pwu4a76md48q8z9uj8s2",
    "omniflix1yq7xj5ceggqdcnq05kr677czw9ctf6mld9z63m",
    "omniflix17phxzzqful67yd7ssmqyfn940ntl7ngugc44fh",
    "omniflix1xfkfc9x7pax4c4wu7mxrq6cst7reddqf3ghy2v",
    "omniflix1g5lmzrrecpfknd2vp6qwzj48ejk6pgeewkwg4x",
    "omniflix1j8jd7tp68my4sp9jjulfwfprw333ck0ekgkt6a",
    "omniflix10llag2qx545mayd5cy0kxv0ndkzcjd5kjll5kw",
    "omniflix1ne8nzq60cvkky8c3dq00damt6lvnm9hfjyek7f",
    "omniflix1e09wgvj4lypvyg4qz5utdrdtff0zasqks9wh25",
    "omniflix1fwszd4p4xldx2yqf37v2929nt6vfy0d0m27mze",
    "omniflix1kjtmkagp4fz7tx9nsu5a2xfnz6m50nudfl384v",
    "omniflix1azrjw348fw2uy2ycgmyk3xrm3tg3gl3d4eecy",
]

# Seed has been taken from random.org: 488127465 ->
# 488127465
# Min: 1, Max: 999999999
# 2023-05-12 19:59:38 UTC

seed = 488127465
np.random.seed(seed)

winners = np.random.choice(list_of_wallets, 1, False)
print(f"The winning wallet: {winners[0]}")
print(f"Congrats :D")

# The winning wallet: omniflix1xuwl7x8htyl26t7pe3l0x6auj3j9jwd2lguy6m
# Congrats :D
