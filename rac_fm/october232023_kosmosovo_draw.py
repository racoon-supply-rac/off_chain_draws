# Draw 3 addresses from all the addresses.
# Each address has the same chance of winning.

import numpy as np

list_of_wallets = [
    'stars142cvfqqkew57awj8xh47agz98qsz987e5unuws', 'stars1ssfrydv7qs6qfnx28q7kmkuvuyea724lnwuv2j',
     'stars139a4n6w6dhwv60dj2clgwm6r0q84gju28z9at0', 'stars1eck27qefttt5twxsg38gsr0q0hr4e3vvxg0vvc',
     'stars1flhs29gr32y3xywvxuzqxymu5pgvyyat0r5epn', 'stars1cvg5dsprer8c7xl0cl966qq0emnjthtwwh4994',
     'stars1eu63507y6zpk87xs99dsvmxdc5cjmgwvgj6qms', 'stars13vk23rl6hmswvwexd9f5ae59egtqy2p7y3glqc',
     'stars1jtzmwppdadmyhv6j68dujwghrp8gkr8skt4jyj', 'stars1e68ds5qu20wxjceeaefn3wxxd698kt97288mcg',
     'stars1c347zr3z9ck7kwf9csxnn5vj5d06xcngxpcpqu', 'stars1rpnqgfdr79zv7zn6d8y888u7vqvpgtr5cqdnuw',
     'stars130qze0dfjuq5g7fazgtlwt2m02al4d7anwsxqj', 'stars10a29hu7chl55ar4wsyjueqxc7smudpvrjlh53k',
     'stars1vuq9jaytesqkwm69h3mlnjdwr9atmjxpyvdgj9', 'stars12x8rq20f3dwuv4wnuwgapn2hjgddech7yf69us',
     'stars1me6xrxj80cp4smrmy2mwaan67spnsen9yn3kry', 'stars1cvcgcvgylrvget5cw9v7q8ghv0fxvyws4vkfcj',
     'stars1jzt962czzt3ruwsapec9fzmrm7kcj442vjk36c', 'stars194mctzam6z69ga68485vrusw5knrcs56zz70fr',
     'stars1fvnn96kq7xex7t365ltva3msu6ewntxf6ur826', 'stars1j6ehrzsmwcg7mjje8m34qmnj6txu8v58plu84x',
     'stars1kcd9zcjzsc5d95hh5ce3ntx0ex24q8cu0sw789', 'stars1m0lzncae2g6shh44j2085rz2ch4ne5q5f3nxpg',
     'stars1jw4heeq5sp0fypvx2aejlppu2pmjxsx9vy20z4', 'stars1ltj4t7hp9x0cq693ldhprkhgrl2cpcvhgkaa6z',
     'stars17rfxutps8ygy8vkemn5cyntv7pzq85xkaqws3d', 'stars1dzxmxc929v5wwl6ch6yu0nvrf5erqecdeq8gs9',
     'stars1ctq6esla3d299l3768g8329uxghpry2mkxfjka', 'stars1zqrqju2txhnnwtgn0d2jutnassmg973322nzsu',
     'stars1u8pad9dtjk5v36sgyj862hehqmfyuukyc78ef6', 'stars1c7ur4tzr4haaqm6ekql0hf4dwwhlvapzx4n5ju',
     'stars1eqntnl6tzcj9h86psg4y4h6hh05g2h9nt08gmq', 'stars1n50lj4k8h0aruzyrfvtaltlvq34zhwrexn9lvt',
     'stars1xuwl7x8htyl26t7pe3l0x6auj3j9jwd2k26qx5', 'stars1j6yw6aldlctpaz2na3awsnexle3a8k6z8x9744',
     'stars1rvkwq3tdfj7u3y8mwk84vcmr063v3xtv2pjghj', 'stars13snvtmj26n6jyt79etf4vejezuqk8v0dt6a735',
     'stars1kqtu5swvgzqqe6es7l6sj82swg7g37l5vfryhg', 'stars1ljjelkegkjz0gz9mcrmkq34rw082zsscpvwsrz',
     'stars199dm0ugv50k4qgcsxjc8p2rertstltxvkddcc6', 'stars1err5c2tc8ha6qa42tpvedgk585dpj35576ny29',
     'stars1849kvwhvf0nqw2lqkjyz36unv3m806rlv73agp', 'stars1fhnc5vtxeclsqpkk8puyx4vmcuxypps0q3d9na',
     'stars1tkgyd0c0pjdxcu6f7z4h8g65whvdcsqhlhwguj', 'stars1qaphxxcc6gg0023cnv6n05yrkkns60kea3xrd2',
     'stars1t8yjrr0egrdffad42yz6ka5vvne3lkt55hjld8', 'stars1akkxnrnmy2c5sazxyz22e8j0p7984y9rz2w78n',
     'stars1r2ullmtu3nwxxt3fmt6kyq6zq3k2cqyx2cddc8', 'stars15zes95rmpr6wg8pd3w7fncp6zqd7vhyfh3pyn9',
     'stars1v5ft27rre0m3th7etfvm5c8vhw462vh672yd66', 'stars188rs3nnqnp6nyc3cyrx0p8ly4tdcwgsf4zs5ml',
     'stars1hwvj0a8hmtlq8593qthsu0r748y4kek2fy9cyh', 'stars17l9zzteq0yjt4mfr7wdk6l94p4u32uan4cvp4t',
     'stars1ng7nu0yqg4vl747khhez4j383d8e9ehh3f9zaf', 'stars139d8eudtzyh9e8nr8kqqexhjjzy77em6ygm470',
     'stars12qyhdyt53qhd2lace09mw6yf24upprthaaugja', 'stars1cx2xj6gw4we6jxxq2s2nc8lfxwwcvejm4j7tx5',
     'stars1fcjfkaxndx26zua4k6vfca8vnrayt23c0z53qd', 'stars18s3zsaz5pls3n7kcgkndfqkvhx544cc5wyj6wh',
     'stars1ey0zmwryem278r7rfhj90uxfuq4ndl9jwpnrgv', 'stars15j4ph8490rumevnlaxtz6cjt37xafz22hsrcwy',
     'stars1whusey8z9vtv8wcqeu9e8njhancxlptf23nwdu', 'stars139q5rxgcc6xa5rt7mqwzepvmhwtqm8x47lzda5',
     'stars1dcuffk2efqtujxqjhwcpn90py305mnfuww8cgf', 'stars17kzy2pya7d5anuvnh0evnq8dgjv32yv3fd5n96',
     'stars10lnxkvncgdxqv8z8aee9pvyf9h8ddcmlzfzg0g', 'stars1sezunc9x6zwqldypxnn26r9mkqvvlr95fx9zsg',
     'stars14ume9hru7ggfsgg560exxf8tyk4hvg7q8u3vy2', 'stars1fpr70ct7yxjajlwqftuxramwsp3v9etekqtsqj',
     'stars1z5x07m62laz6thm8quanqgvg42gz99s833eaqw', 'stars1v0ulf080nvcfu36ln8t6rkr4mg45mks3q952ag',
     'stars1svfpddvanq0p4ejp0v9myxt5zrfy6mdyxjd29n', 'stars137p2qrs3qw00c28679pwu4a76md48q8zv75rv9',
     'stars1wmvvnk6gx6gkknvegslgrydmsx2khrdt8jz5xt', 'stars1sqawrkskx9wezx47vygf3nm2szqrhh2a8kdvuu',
     'stars1lh6ruf253fhjykdesvfccy0y0vhjque4uwcey3', 'stars1rk57hh3nsnqre55h44q2zn76f57q39gewxvn0q',
     'stars1a372k7l9gpcz6fyzjahrnq4d4zxqashvh53auy', 'stars13mzcw7ezlgzcgpls7xqxpsg5qqsxvp8je5fehz',
     'stars1jvm8gy4lgzcrsagxpyhvvxymz982y3j58xg6sr', 'stars1p4jtl8yadqmjcqz548hshgnp8kfxjtp5lutn0x',
     'stars16ja5akn8pmcc44z09ahtd06zqd8lwrmltucdhy', 'stars1zp85ttd08kugkwjlratq2mqfk87vm9ztdygvlz',
     'stars1aphlrx49zy59tfh5cj629q3s2jzr88huhn6dkd', 'stars180xy8rlhpvlxcjw3x9rse83c0d2266nz9w54t8',
     'stars1aweyhgzz6y3yak5whspuzwfly3zgsjtu9ph7pk', 'stars1dqsmw3sryd4f8ty8sl455ym6usznmdvlryggtz',
     'stars1ylx03vqp2zkpjayudpx2k0psgdx4uc3dz5wq5j', 'stars13rmr9lhdxvmpul4zzuqr49l33mz5asj85azk2h',
     'stars12kzmjhx6sdc8vdya9jd7nvmjmqqwhfrtrtvzvy', 'stars1mlk9mrufard8r23vlagqdcvytlswwhtvrss87v',
     'stars1eczxwqx3qs5gz3mwl3er9gxd6aa3kf7egz8vtk', 'stars1958ex963n93nhmvcrtlwwtr0c9qmvewhsyalzw',
     'stars1zr6mvjs6ee4ryhqeanaqn8g93jrjhn9sptup0l', 'stars1c6srhjx6tqj2m3q2hpwt8dnkde0wrmvhmzezzy',
     'stars1lvrgkxm0gzvsh2ruve02k3tq3dv3fce3p5pad9', 'stars1rxtlgc5xw9anlkasady7ukfrppktl950ht2pv9',
     'stars1442jxc2sdh0rpw20lt0w2gep50kypjy3culxc2', 'stars1zhv6enwzn04gsx70755xluxs6n62fwxjzaea4c',
     'stars1q3tz46plr7hsx3qzdssv5f5wy94av3m367uaf2', 'stars16xqf05lggllk363x7gppll5x8jh7yz89s8jnjp',
     'stars14q4c6kgg7xegcc88naqt6f8fz2skuzczhtg87f', 'stars1c5dzyr8v8z7c5hzygsj4w6mxadatj49knzhetn',
     'stars19fumfhgfvp2q7lffvaypwwmuz93wfrdspugey0', 'stars13a6nz8mej9e9gur525x6d2hfw0ql027nnk65yj',
     'stars1jpfxkmj6ycehtpmu7gc5s7rg3mppwvm57uf846', 'stars1mdcg8trzh25k9kjfze5eahdzezaf8qanjfwvjg',
     'stars1zpl9rasg8qh3nucxcy67evq7nlhg08ec95lcyn', 'stars1j8xcf9yuyjlr9p5qpnwrplvxqjc3ya4fcvexds',
     'stars1v4y00p0t2raap3gqrm8zqn7wmfc3pnyetwaaje', 'stars1akjk279tmjzfk94n69a4j9w68dggpvjw2sx0xh',
     'stars1yz4wmwawc50755s5k44v24cqp607yawmxa7t69', 'stars13pdwypz3qepfzva82cy75vw4c5vk5namq4wxlg',
     'stars17nun6cg7a5xtu9fz2p8scxr7u9jmrf5vcg5rua', 'stars1yvjzddtyg5jt2vruea0wgyqae9dwqy3d20p0fw',
     'stars1zm8epp3rul4lsu47szwmjcuxxa5xekgfhgwprk', 'stars1spkrjuxqucvrtg4433ep3mdmz3h5eewhx2kkvj',
     'stars17fzx4rvw04586s8f2c2vv53pe3yypu0c6jqukd', 'stars1kuy7rxj8t23l0zpt4l36rzsq430wdnxfnjkfwx',
     'stars14hhtkr6tcfg0l9ecy55dzn4maq5ufjerjmctpr', 'stars1mwh6pm9c043rcfjd5np5hpjvf9umsmag86xy28']

# Seed has been taken from random.org: 530742272 ->
# 530742272
# Min: 1, Max: 999999999
# 2023-10-23 11:53:17 UTC

seed = 530742272
np.random.seed(seed)

print(f"Drawing from {len(list_of_wallets)} addresses...")

winners = np.random.choice(list_of_wallets, 3, False)

for idx, winner in enumerate(winners):
    print(f"Winner #{idx+1} -> {winner}")
print(f"Congrats :D")

# Drawing from 122 addresses...
# Winner #1 -> stars1mwh6pm9c043rcfjd5np5hpjvf9umsmag86xy28
# Winner #2 -> stars1ng7nu0yqg4vl747khhez4j383d8e9ehh3f9zaf
# Winner #3 -> stars1zr6mvjs6ee4ryhqeanaqn8g93jrjhn9sptup0l
# Congrats :D