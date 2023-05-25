# Draw 1 address from all the addresses

import numpy as np

list_of_wallets = [
    'stars1w93f099t4pp9jamyghp88p60fvkg39dx92tufd',
    'stars1fpr70ct7yxjajlwqftuxramwsp3v9etekqtsqj',
    'stars1a48wdtjn3egw7swhfkeshwdtjvs6hq9ntc5nh6',
    'stars1glg3w36a7mzc82rpvn0ac7dv3uv6l0nwytnmtp',
    'stars1vlr5h5s34heq29g4ea6dzluljz48xaujtpna3l',
    'stars1ldyxnnw5pl3l00849nvyw5vulpj6w8sadwp8hc',
    'stars1lzpz72s3gz3vhrtap4vmcuz4daf8nf3v0aes4h',
    'stars1agege7zerzcqm7lhc5j5ppzf8quetev48yccpf',
    'stars1sah6yh3jmx8z24jgnytsurqryfrx5sqwuvqd9r',
    'stars1hce9n95e33qplgxujezffsv0sauj9x0ccv0xcq',
    'stars1flhs29gr32y3xywvxuzqxymu5pgvyyat0r5epn',
    'stars1q85k7an4hwkwhfjcxtkkn6at5p07cgmcvjxyle',
    'stars17fmhd9esc0g26qttyq9q0kph6ze0445c3rt7ps',
    'stars1v6fnklkj5av596xrv9sucdvcgk7llhra0nf24d',
    'stars1lamfr7ufuflu6l7aukgjnrqzcg4ad277ffp2p0',
    'stars1m7gls9r2mapj9yaasgsvunj8uppern7xh25nj0',
    'stars1mm8huzhpk5tx5vgj877zse37c2zdymzlh57kv6',
    'stars1dy6c2gvg0802ujsnkhcg3f0vuvqwypu3kay4gj',
    'stars194aek5zglzmyjlj8cyt4sdmg7dcmpckwgltfdr',
    'stars1pcsaq68d70ycvdxxv3tdl6uvamhkg9nvqmedfs',
    'stars145kvyy7njm970wu58ytpv38caxl7yvm59kf2ar',
    'stars1x60vqqe0qd0gp3jjevvxq5mzfyzlvqmzp27g54',
    'stars1hheryepdqyamzy4vsh7alcjlwq5k0kfmsusn9v',
    'stars17jvy2a5g9eamn9pcnjqc5eea46wqm9259a7432',
    'stars190t90m7zplw5rrq8v4g9fs0tfpr7mqk8dqj8xh',
    'stars13uu69g2ah5wsw386zf4x9phhk5fk7ryszqfq9g',
    'stars17v6tme9dus6u5gtx4emdgdwqz567pct3celna4',
    'stars1ctq6esla3d299l3768g8329uxghpry2mkxfjka',
    'stars17rfxutps8ygy8vkemn5cyntv7pzq85xkaqws3d',
    'stars10w200jzj5jt0ph3n8l8kfl4zhswf8z6gul8utm',
    'stars1qaunnsdc544tj7cpe4m7uf42khlumvx0x5ulpp',
    'stars1d3ua265kjjn0hu0lnuc06nyp58cl99nqp58wu6',
    'stars1y5eqrhudwkc2uquaz3v429zuqsw4nhjmwnd4cx',
    'stars1hmda69ykt8rzsrxanrxm2r837edln3pjmzmtdr',
    'stars193f29pj2n8zypqxnqryepakue5s0s4h3dd9p4r',
    'stars18e4fdwr23h9j2e6uucvuzsx9gwhys3q07c2jgf',
    'stars1zerql52xeuqhslcyet0ek2g7w3nav9m780k3tv',
    'stars17pe4wffe5n094v9xm3v0jyvj38z3rzuss30lex',
    'stars1snamxl3mua7kzhfr6e2ycm45t2u4phfecd5cvc',
    'stars1pcpwpfe9x54a9gpa33je7su4u983xhfup8dpj5',
    'stars1wc4jn39zgc8cn9869nhfy3p690ax094xe5pg6v',
    'stars1nmuf0yg8krctmg4qr0rdyhvkyhxle0cj4c672u',
    'stars1hdjtzu20egjmwdqlkja3m5gcysx7udr8vjkttm',
    'stars1va2xq5d9lj5v8aakxawgne3chn9phzwlrfr6rk',
    'stars1ul09h68v574lxxpq0z0ds45n5ycx4wkurr4y77',
    'stars1n45552m28f6ep54shzh45txtkff25flahswlpv',
    'stars1zf3e767k5wavvhweypezp6f69f46pp4g7w58yt',
    'stars145l5hu9kt6kevaxm0mg24a2zx0qlrct4hankmd',
    'stars19decgarz7vv072t8cpjh2fvtvzvpv9zvdaplan',
    'stars1v5ft27rre0m3th7etfvm5c8vhw462vh672yd66',
    'stars19s54rjkzta6nan8f89a49sfr44celvqqeh773l',
    'stars1h6vz7mh0zzdagmret5sgzd8c2kwn0k37sz5p6u',
    'stars1neqprx4sd0xrs4snn2q9ccchg6ksva3p0vxcfl',
    'stars1yqxtj0ke9yxn2vjpe0v5gqc5zptfrzex0tluv8',
    'stars19m7yjvyh7s0ffhpe9xlnvz42jhvsgjh63slcwz',
    'stars14w4zt22mfzat46nywf0ntrjzl8g5hu483ds8yc',
    'stars1jt59wglrqhmw08y9appg7cmwxkzu3mddta6ppp',
    'stars195z08s2qj0em8pzyyaqm5l29p0w9vrdesc64sg',
    'stars1a2s6x6p4qdtzjtaleuv86zc7ta0jtjcett2ucc',
    'stars1xjtmgx63hr939alywhc7fh95d6c33gfwf7kwfy',
    'stars103verdnv4pzztty50ua7gs5gj25l2gwud4yz2f',
    'stars19fumfhgfvp2q7lffvaypwwmuz93wfrdspugey0',
    'stars1tg5um3wts76susk3dhn0wh3ymj53e62dlemz9u',
    'stars1lx520st5ctmh4uj2q2j9hq5d0skszkf5f9ts0x',
    'stars154fvcpg0qesfnegljtpvjamr5azw548mty3tg7',
    'stars1waa2shn294wsp6x0nj0cs0ygenemt3wrh4wxqa',
    'stars17s590zs2nwh3ckn5et3925x6khupaecupfq9a3',
    'stars1u7xwld7jrsj3dh8a7chezj8nj2ac36e8e808ku',
    'stars1mk2yasfjljrvrxrjwj5823xh6lctkjc9lq28ch'
]

# Seed has been taken from random.org: 424645858 ->
# 424645858
# Min: 1, Max: 999999999
# 2023-05-25 14:12:20 UTC

seed = 424645858
np.random.seed(seed)

winners = np.random.choice(list_of_wallets, 1, False)
print(f"The winning wallet: {winners[0]}")
print(f"Congrats :D")

# The winning wallet: stars1n45552m28f6ep54shzh45txtkff25flahswlpv
# Congrats :D
