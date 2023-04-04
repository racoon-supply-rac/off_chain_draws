# https://twitter.com/RacoonSupply/status/1642261616052908036

import numpy as np

# 58 entries

# Below are the addresses that interacted with Racoon.Bet using $JUNO between blocks
# 7648000 and 7689000
unique_juno_addr_interactions = [
  'juno1v6f249cla6l4jha4tkm6zu2l43hvxzavjw3ss5',
  'juno17xpfvakm2amg962yls6f84z3kell8c5lxtqmvp',
  'juno13ye4czwvptppx7makqrt578y4tcxg3l2vhnsa4',
  'juno1fn0h75ee5rudwfnuc47nrkqes5pftp373xvrgj',
  'juno1yvjzddtyg5jt2vruea0wgyqae9dwqy3dgp4f9r',
  'juno1xuwl7x8htyl26t7pe3l0x6auj3j9jwd25ywx2e',
  'juno1mql46ppfxjwqljyynja0ea9m2jz5whmh7d87w5',
  'juno137p2qrs3qw00c28679pwu4a76md48q8zwsq9qg',
  'juno1ssfrydv7qs6qfnx28q7kmkuvuyea724l3qg2xl',
  'juno1zg453l326xgrk5nm2prru4teqkym8zc9lsyg7v',
  'juno1z25uywjrzeuvw0rmnhxney4fdcql8d4wk5gdv6',
  'juno16qp4jdlrcl6afaqm43qawsaf57gxc7p83wyrgg',
  'juno1z63r2yzl5gztm03zewl3l3mrlh65gcjsrlffua',
  'juno1f08y7we7qanwnze5ydnkh4kg99xmz8mjfq4ktn',
  'juno1wr8pdqarf933zf6glwt022fhaz8l0tv6llxale',
  'juno1ynecpv64gtyc8s2hh2jze09qapgx7es6fxgyfw',
  'juno16dt8q6zala43dkh66wqy3wzauh44tzjr2pstga',
  'juno1e09wgvj4lypvyg4qz5utdrdtff0zasqkmfu46k',
  'juno16r4n78rw0sqd0u939jlypnvpd08f9ux40j9y0d',
  'juno102h9qge2arxe0xnzk9nj5yqmmdycwjcfvl2tss',
  'juno10a29hu7chl55ar4wsyjueqxc7smudpvrs3rjam',
  'juno1fprwljg0qkgrxgkcudf4g75t7pm05s5kle68cm',
  'juno1k9cspanymj2ffl576lgtp865dnfedqzwsrzsfh',
  'juno17j9rqfx0de7uzdv40z3eg5d9d6yf2se9s77k7v',
  'juno14hew5e5ua5pzhr6swnr0t2md6up7qmgpe36s35',
  'juno109tnw70rafe458nd3k8qrn6xpan6tnx0vcac7h',
  'juno1r4thrg4c9crc2e2lppx07dhu04x26xden37c0p',
  'juno1mk2yasfjljrvrxrjwj5823xh6lctkjc9aw7p56',
  'juno15f03t4k7xfpth3cmw58966s4t88rf9emdgrmky',
  'juno1phjay9jyx7wty20qpts2t78eqq22dvaqy3hl5x',
  'juno1zfh6ccddln9e4fkwse7fcquvecpnnxyk334jwz',
  'juno1us8zmnqkravc378evmdxxjt7kksauv5ec7zf8a',
  'juno1z2g00a8xsupge8km9pfs9auzu49vkmk59k6uw6',
  'juno1dmzy923gxqfatz9ea68e7d5w07f7tkfz6fxks2',
  'juno10u7edzpnkssaaxtumd442hpv2dfn4gvq2tg4f0',
  'juno1lq9h2undsu8eq5vzzeuqu98cgu5pkp73ftg8x8',
  'juno15zes95rmpr6wg8pd3w7fncp6zqd7vhyf4l4zlg'
]

# Below are the addresses that interacted with Racoon.Bet using $RAC between blocks
# 7648000 and 7689000
unique_rac_addr_interactions = [
  'juno1mql46ppfxjwqljyynja0ea9m2jz5whmh7d87w5',
  'juno1xuwl7x8htyl26t7pe3l0x6auj3j9jwd25ywx2e',
  'juno1vv2nm8tvpyx88r07hx5x4zyctpkztp6yx9uwzu',
  'juno137p2qrs3qw00c28679pwu4a76md48q8zwsq9qg',
  'juno1f08y7we7qanwnze5ydnkh4kg99xmz8mjfq4ktn',
  'juno16r4n78rw0sqd0u939jlypnvpd08f9ux40j9y0d',
  'juno1ssfrydv7qs6qfnx28q7kmkuvuyea724l3qg2xl',
  'juno10a29hu7chl55ar4wsyjueqxc7smudpvrs3rjam'
]

# Below are the addresses that interacted with Racoon.Bet using $HUAHUA between blocks
# 6788000 and 6831000
unique_huahua_addr_interactions = [
  'chihuahua1dz5xhrk76rkc6sa9u2gurhqthtdt9w7w6a2nlz',
  'chihuahua1qqnlsrpk5uhf6ktdq08g52tjeqmlmrsyxc42a5',
  'chihuahua109tnw70rafe458nd3k8qrn6xpan6tnx0elndcf',
  'chihuahua15xvalgjv5rs57ghjvyc7tcyadjmsj8j8a242q6',
  'chihuahua1k5w5fpu3qt4va27vsarddnruumqqprs84a6s9q',
  'chihuahua137p2qrs3qw00c28679pwu4a76md48q8zmhwsxk',
  'chihuahua1yvjzddtyg5jt2vruea0wgyqae9dwqy3daxmura',
  'chihuahua1skfk48l5mu2hyhpvxgue2kg4rjgeax2cs7fet5',
  'chihuahua16qp4jdlrcl6afaqm43qawsaf57gxc7p8yf2kwk',
  'chihuahua12nr0nu5k8uxyg2g0ra75elqsn4my5mjk2y3dzh',
  'chihuahua1fdfgyjjdx2xffzctjzgmvpp5spakj8gq2fa8an',
  'chihuahua1ah3d4d67lx3qkudl3wmfu9f63cafw5fu6y8s0e',
  'chihuahua1yfgvyv3jxact4l6vkdfs0kdtsfvkd0chs2h8pv',
  'chihuahua1ktvnuysk4lz0westx7wg9q6rggz8e59z2wfd5l',
  'chihuahua1kj2z2cjvw7kuxpj22ann0s2wmg03a4p5j96w53',
  'chihuahua1xwseskrmnxrvesmad0xtyfvl3lx7xzkkg570hz',
  'chihuahua1z58lfqa2005hs34qupar265v3e6crf6xlzrdxe',
  'chihuahua1wr8pdqarf933zf6glwt022fhaz8l0tv62cgge8',
  'chihuahua1z2g00a8xsupge8km9pfs9auzu49vkmk5s35fgy',
  'chihuahua1hc0jvwtxxm7af2yydzdzs5scufum86uwcp8cza'
]

list_of_all_addresses = []
list_of_all_addresses.extend(unique_juno_addr_interactions)
list_of_all_addresses.extend(unique_rac_addr_interactions)
list_of_all_addresses.extend(unique_huahua_addr_interactions)

# Seed has been taken from random.org: 538207131 ->
# 538207131
# Min: 1, Max: 999999999
# 2023-04-04 14:36:18 UTC

seed = 538207131
np.random.seed(seed)

winners = np.random.choice(list_of_all_addresses, 10, False)
print(f"Winners are: ")
for winner in winners:
    print(winner)
print(f"Congrats :D")

# Winners are:
# juno1f08y7we7qanwnze5ydnkh4kg99xmz8mjfq4ktn
# chihuahua1yfgvyv3jxact4l6vkdfs0kdtsfvkd0chs2h8pv
# juno1fn0h75ee5rudwfnuc47nrkqes5pftp373xvrgj
# juno1dmzy923gxqfatz9ea68e7d5w07f7tkfz6fxks2
# juno1mk2yasfjljrvrxrjwj5823xh6lctkjc9aw7p56
# juno10u7edzpnkssaaxtumd442hpv2dfn4gvq2tg4f0
# juno109tnw70rafe458nd3k8qrn6xpan6tnx0vcac7h
# juno1k9cspanymj2ffl576lgtp865dnfedqzwsrzsfh
# chihuahua1k5w5fpu3qt4va27vsarddnruumqqprs84a6s9q
# juno16r4n78rw0sqd0u939jlypnvpd08f9ux40j9y0d
# Congrats :D
#
# Process finished with exit code 0
