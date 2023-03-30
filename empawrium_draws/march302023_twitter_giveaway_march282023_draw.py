# https://twitter.com/RacoonSupply/status/1640699248378359814

import numpy as np

# 92 entries
list_of_rter = ['@Bitjoint2', '@MonsieurP4n4che', '@cosmaras', '@dk642', '@chestercarneva1', '@misairdrop', '@raden_jb',
                '@sir_arndt', '@DirtyHairy71', '@alsahhim31', '@0xponci', '@Moby_Duck_420', '@cc0826d4c0bc4a2',
                '@Dal_Alkis', '@Klemennns', '@dew_on_roses', '@skeetstake', '@ASully1115', '@aji3003', '@mikku31',
                '@m4n_bonanza', '@Yiouhou2', '@KimLamminger', '@1989MUERTE1989', '@CriptoAlegria', '@bobbybailie',
                '@sekt666', '@SharonFit11', '@ChiapFed', '@cryptow00t', '@giorgis_crypto', '@ZapdosRAC', '@DizzleSocial',
                '@Faniscrypto', '@crypto_pupa', '@MaxPain47209603', '@beartowngiant', '@Intern_Cosmos', '@BlarcSam',
                '@Seannom1', '@Fakk2', '@BDcrypto_', '@GhostOfCalitha', '@BrianCh48272927', '@CButtasang', '@GregWeld',
                '@rithmu', '@TheThorLady', '@Rydog760', '@mossel2022', '@MoonixLoL', '@passioncyp', '@BushidoBrown28',
                '@gigibitcoin', '@DonDon14321', '@psyccccc', '@Raswid', '@qlionex', '@SonyXpe41357662', '@HUAHUA_S6',
                '@cryptocosmos84', '@us3l3ssch1', '@aldibradiiiiiii', '@KHUNFI', '@SiriusSquatch', '@Mysticism88',
                '@godbout_ct', '@seekingheal', '@makitango1', '@crypto_fun_fun', '@ReigoluckyMegan', '@SmileysNetwork',
                '@NftChihuahua', '@lucasdosrl', '@fightfarmbetz', '@emileadipura', '@lilgainzz', '@Welding_Cosmos',
                '@KhadijaKabirAb4', '@paplianos', '@_wolfbytes', '@doglife420', '@homestead_cosmo', '@Elli25156191',
                '@mathgril', '@brucemanRAC', '@WHiTeRHiNo_420', '@jbertter', '@Rarma_', '@xReactor_', '@0xMeeessien',
                '@Ser_cry1']

# Seed has been taken from random.org: 83552030 ->
# 83552030
# Min: 1, Max: 999999999
# 2023-03-30 13:23:47 UTC

seed = 83552030
np.random.seed(seed)

winners = np.random.choice(list_of_rter, 2, False)
print(f"Winner of 100$ is {winners[0]}!") # Winner is @chestercarneva1!
print(f"Winner of the Psychedelic Chihuahua NFT is {winners[1]}!") # Winner of the Psychedelic Chihuahua NFT is @mikku31!
