# https://twitter.com/RacoonSupply/status/1642261616052908036

import numpy as np

# 74 entries
list_of_rter = ['@WingsWorldNFTs', '@LuisDake', '@mrs_cosmoslin', '@Weierstrass13', '@surestboy10', '@OyinsSimply',
                '@IFNScouting', '@doglife420', '@TimiNewton', '@bobbybailie', '@Madman_Crypto_', '@RoboVerseWeb3',
                '@sekt666', '@Swindley37', '@robsondsdm', '@Ambedo_Bass', '@Inn_a_Dream', '@The4thIR', '@evmospace',
                '@Esteerluv', '@donlu55', '@Dennistough', '@mikku31', '@Bitjoint2', '@Ns_JNR', '@ChainofAtom',
                '@smartbadboi', '@MaxPain47209603', '@aji3003', '@us3l3ssch1', '@denfatuf', '@BushidoBrown28',
                '@KimLamminger', '@redcodder', '@ReigoluckyMegan', '@ZapdosRAC', '@ChihuahuaChain', '@hatori79',
                '@stahly85', '@Hubatec', '@brucemanRAC', '@aldibradiiiiiii', '@cosmaras', '@dew_on_roses',
                '@Tedk42069', '@Ghostboyxy', '@alsahhim31', '@Mickeypirson', '@griseldabllanco', '@Faniscrypto',
                '@ChickzMeta', '@junioroyindeny1', '@Evansmighty1', '@DrBittcoin', '@this_istony', '@WHiTeRHiNo_420',
                '@MichaelTea1129', '@KemsiAwiz', '@LaVidaDelCrypto', '@M42Pavlo', '@Keios23', '@spicygurl444',
                '@poubenijosephi1', '@fightfarmbetz', '@Wing79345156', '@SiriusSquatch', '@1989MUERTE1989',
                '@Doyley2380', '@Mannyrs13', '@Scott59021942', '@homestead_cosmo', '@DonDon14321', '@bigwin_aka',
                '@Mich_crypto1989']


# Seed has been taken from random.org: 538207131 ->
# 538207131
# Min: 1, Max: 999999999
# 2023-04-04 14:36:18 UTC

seed = 538207131
np.random.seed(seed)

winners = np.random.choice(list_of_rter, 10, False)
print(f"Winners are: ")
for winner in winners:
    print(winner)
print(f"Congrats :D")

#Winners are:
# @junioroyindeny1
# @Mich_crypto1989
# @griseldabllanco
# @redcodder
# @DrBittcoin
# @stahly85
# @aldibradiiiiiii
# @homestead_cosmo
# @poubenijosephi1
# @surestboy10
# Congrats :D