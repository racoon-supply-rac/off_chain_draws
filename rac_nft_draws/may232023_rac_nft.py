import numpy as np

# list of retweeters
list_of_retweeters = ['OstrowskiArek', 'sia_CN_', 'Nikson_SinGrom', 'Dennistough', 'BryanJimenez21', '85_alchemist', 'goguokuo', 'denthinker', 'The5thForce0_0', 'okshock', 'LuisL3D', 'lol_alif', 'homestead_cosmo', 'thabbest', 'brucemanRAC', 'MagicMarWolf', 'DonDon14321', 'Intern_Cosmos', '0xponci', 'MJRaymond89', 'Migalunatic', 'StashhApp', 'ScrtScrappy007', 'shakirmayo47', 'scrtlovers', 'WingsWorldNFTs', 'Jsmiles207', 'Marti130719', 'ZapdosRAC', 'junioroyindeny1', 'mejiamarilyn33', 'IgbongQ', 'cung2812', 'durokad', 'CyptoShaman', 'BushidoBrown28', 'SecretRobertino', 'Madman_Crypto_', 'Inn_a_Dream', 'Caroline8201', 'TimiNewton', 'matt_arn', 'SiriusSquatch', 'xoreka', 'Ghostboyxy', 'Cessyderama', 'surestboy10', 'The4thIR', 'dew_on_roses', 'JFitz_', 'GregWeld', 'beartowngiant', 'DefiDon_eth', 'TuanLuong19', 'MoltresRAC', 'redcodder', 'blueroses161', 'shrute_buck', 'FurryRafiq', 'passioncyp', 'haidarchughtai', 'pjsoga', 'cosmosecosystm', 'AdamPFarnsworth', 'Degentime420', 'mrs_cosmoslin', 'Cryptome1', 'poubenijosephi1', 'Hamza3808392373', 'ReigoluckyMegan', 'babywolfe25', 'denfatuf', 'jamessatoshi1', 'lilgainzz', 'Firefly_808', 'selaets', 'stahly85', 'lunar391', 'Qweenthebest', 'gerkolan', 'mlazaro881', 'GreenGoldArmy', 'BansalCrypto', 'GameplaysLoco', 'HooliganDegen', 'Waluwp', 'spicygurl444', 'Bl_ckkky', 'John43148935', 'cosmos_ahmed', 'griseldabllanco', 'outsidemind', 'KemsiAwiz', 'DrBittcoin', 'CVCVCPCP', 'Blessed_nife16', 'Sarah_Sara4', 'JonOmega1', 'smartbadboi', 'EvgPash', '_Cypriot', 'godbout_ct', 'BilalRMK', 'Devchiemerie', 'X269IndigoMAFIA', 'makitango1', 'Zakacometh', 'bsesscrypto', 'DebeshKumarDub2', 'SABEELNFT', 'MaciejGeolog', '_erikio', 'Jistsos', 'Donguri_5555', 'superman__171', 'Esteerluv', 'GirlSamantah', 'heesanhunt', 'Qwin_Erica', 'HollinsCrypto', 'AGorgolit', 'mr09873643', 'evmospace', 'CosmosShah', 'MortimCrypto', 'donlu55', 'RektChente', '0xosmozone', 'EHotta', 'fightfarmbetz', 'MaxPain47209603', 'residentcosmos', 'HosonKwok', 'WHiTeRHiNo_420', 'y_dist654', 'adnanshakir604', 'manliketochii4', 'zhafi_NFT', 'Chaosmos89', 'EveNasle', 'JasonSopko42', 'Evansmighty1', 'LuisDake', 'Ownyourplace', 'DizzleSocial', 'guillen_fajardo', 'Thanasi69473216', 'gigibitcoin', 'iammonurohila', 'VvZeass', 'korki_4', 'Moneytree_IBC', 'Bitjoint2', '_wolfbytes', 'aji3003', 'Vinyl_roy', 'RAC_FM_Spaces', 'Ambedo_Bass', 'imBackBrody', 'shah_rukh_rao', 'jbertter', 'kiddwaya11', 'RugMeBro', 'aldibradiiiiiii', 'alsahhim31', 'nuisthiwanu', 'sir_arndt', 'ChainofAtom', 'votor1337', 'G_Slade', 'uchin_febri', 'TMetaverseClub', 'OyinsSimply', 'KimLamminger']
list_of_commenters = ['passioncyp', 'GirlSamantah', '_wolfbytes', 'Bl_ckkky', 'Thanasi69473216', 'manliketochii4', 'BushidoBrown28', 'GregWeld', 'MJRaymond89', 'DizzleSocial', 'guillen_fajardo', 'JFitz_', 'jamessatoshi1', 'FurryRafiq', 'beartowngiant', 'KimLamminger', 'griseldabllanco', 'EvgPash', 'selaets', 'John43148935', 'GreenGoldArmy', 'thabbest', 'brucemanRAC', 'WingsWorldNFTs', 'goguokuo', 'SecretRobertino', 'makitango1', 'uchin_febri', 'AdamPFarnsworth', 'sia_CN_', 'MaxPain47209603', 'Waluwp', 'nuisthiwanu', 'heesanhunt', 'Marti130719', 'shakirmayo47', 'Sarah_Sara4', 'okshock', 'DrBittcoin', 'SABEELNFT', 'Qwin_Erica', 'aldibradiiiiiii', 'RAC_FM_Spaces', 'lol_alif', 'cosmosecosystm', 'Degentime420', 'Qweenthebest', 'pjsoga', 'Hamza3808392373', 'EveNasle', 'shrute_buck', 'residentcosmos', 'Inn_a_Dream', 'CVCVCPCP', 'korki_4', 'iammonurohila', 'Intern_Cosmos', '_erikio', 'X269IndigoMAFIA', 'JonOmega1', 'Devchiemerie', 'votor1337', 'mrs_cosmoslin', 'Madman_Crypto_', 'EHotta', '0xosmozone', 'Zakacometh', 'Cessyderama', 'evmospace', '85_alchemist', 'zhafi_NFT', 'Migalunatic', 'LuisL3D', 'ReigoluckyMegan', 'Nikson_SinGrom', 'kiddwaya11', 'BilalRMK', 'The5thForce0_0', 'GameplaysLoco', 'bsesscrypto', 'scrtlovers', 'homestead_cosmo', 'aji3003', 'sir_arndt', 'ChainofAtom', 'DonDon14321', 'ZapdosRAC', 'CyptoShaman', 'Chevallier17', 'Cryptome1', 'outsidemind', 'RugMeBro', 'superman__171', 'lunar391', 'Caroline8201', 'ScrtScrappy007', 'dew_on_roses', 'shah_rukh_rao', 'G_Slade', 'cosmos_ahmed', 'AGorgolit', 'Donguri_5555', 'RacoonSupply', 'SiriusSquatch', 'stahly85', 'VvZeass', 'fightfarmbetz', 'IgbongQ', 'CosmosJunky2', 'OstrowskiArek', 'Bitjoint2', 'DebeshKumarDub2', 'jbertter', 'Ambedo_Bass', 'Chaosmos89', 'The4thIR', 'blueroses161', 'Firefly_808', '_Cypriot', 'mr09873643', 'adnanshakir604', 'HollinsCrypto', 'MortimCrypto', 'MaciejGeolog', 'WHiTeRHiNo_420', 'redcodder', 'mejiamarilyn33', 'CosmosShah', 'alsahhim31', 'godbout_ct', 'RektChente', 'denthinker', 'MagicMarWolf', 'Moneytree_IBC', 'haidarchughtai', 'gigibitcoin', 'DefiDon_eth']

# everyone in the retweeter have 1 tickets and those who also commented have an additional ticket
list_of_everyone = []
for element in list_of_retweeters:
    list_of_everyone.append(element)

for element in list_of_commenters:
    # making sure it was retweeted as well
    if element in list_of_retweeters:
        list_of_everyone.append(element)

print(f"Total tickets: {len(list_of_everyone)}")

# Seed has been taken from random.org: 167399208 ->
# 167399208
# Min: 1, Max: 999999999
# 2023-05-23 21:24:23 UTC

seed = 167399208
np.random.seed(seed)

winners = np.random.choice(list_of_everyone, 1, False)
for winner in list(winners):
    print(f"Winning user: {winner}")

print("Congrats :D")
