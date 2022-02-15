import web3
import json
import csv
import sys
import numpy as np


contract_address = '0x892555E75350E11f2058d086C72b9C94C9493d72'
contract_abi = '[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"previousArweaveHash","type":"string"},{"indexed":false,"internalType":"string","name":"newArweaveHash","type":"string"},{"indexed":false,"internalType":"string","name":"previousIpfsHash","type":"string"},{"indexed":false,"internalType":"string","name":"newIpfsHash","type":"string"}],"name":"GeneratorUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"dudeID","type":"uint256"},{"indexed":false,"internalType":"string","name":"previousName","type":"string"},{"indexed":false,"internalType":"string","name":"newName","type":"string"}],"name":"NameUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"activateSkills","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"baseURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_basePrice","type":"uint256"},{"internalType":"uint256","name":"_traitPrice","type":"uint256"},{"internalType":"uint256","name":"_freeTraits","type":"uint256"}],"name":"changePrice","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getArweaveGeneratorHash","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getArweaveImgHash","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"getIpfsGeneratorHash","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getIpfsImgHash","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenID","type":"uint256"}],"name":"getName","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getRemovedTraits","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getSkills","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getTraits","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"newName","type":"string"}],"name":"isNameAllowed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"string","name":"nameString","type":"string"}],"name":"isNameReserved","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"traitCombi","type":"uint256"}],"name":"isUnique","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pauseMinting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"singleTraits","type":"uint256[]"},{"internalType":"uint256[]","name":"bodyTraits","type":"uint256[]"},{"internalType":"uint256[]","name":"dresstop","type":"uint256[]"},{"internalType":"uint256[]","name":"dressbottom","type":"uint256[]"},{"internalType":"uint256[]","name":"accessoires","type":"uint256[]"}],"name":"purchase","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"baseURI","type":"string"}],"name":"setBaseURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"newArweave","type":"string"},{"internalType":"string","name":"newIpfs","type":"string"}],"name":"setGeneratorHashes","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpauseMinting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenID","type":"uint256"},{"internalType":"string","name":"newName","type":"string"}],"name":"updateName","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
infura_url = 'https://mainnet.infura.io/v3/84f252b2d9c243babf869ad9df78484c'

traits_file = 'traits.csv'

trait_groups = {'left hand': ['skateboard', 'owl', 'ananas', 'piece of shit', 'sunflower', 'ice cream cone left hand',
                              'bloody golden knive', 'violet hookah', 'red balloon', 'dumbbell in left hand',
                              'bloody sword', 'green bottle', 'trident', 'pitchfork', 'crowbar', 'rifle',
                              'money bag in left hand', 'black brief case', 'dynamite', 'default left hand'],
                'right hand': ['fish', 'boombox', 'walking stick', 'cactus', 'ice cream cone in right hand',
                               'magic wand', 'tulip', 'knive', 'basketball', 'green hookah', 'blue balloon',
                               'banana', 'dumbbell in right hand', 'sword in right hand', 'beer in right hand',
                               'brown bottle', 'letter', 'anchor', 'leather briefcase', 'money bag in right hand',
                               'default right hand'],
                'shoes': ['black boots', 'pink boots', 'orange boots', 'white boots', 'sand boots',
                          'yellow rubber boots', 'green rubber boots', 'sandals', 'blue uggs', 'green uggs',
                          'sand uggs', 'brown boots', 'black loafer', 'brown loafer', 'violet sneakers',
                          'yellow sneakers', 'white sneakers', 'black sneakers', 'green sneakers', 'red sneakers',
                          'grey sneakers', 'black cowboy boots', 'white cowboy boots', 'brown cowboy boots',
                          'default shoes'],
                'hat': ['red bobble hat', 'blue bobble hat', 'cook hat', 'prison hat', 'police hat', 'crown',
                        'black beanie', 'green beanie', 'white beanie', 'red beanie', 'white cowboy hat',
                        'brown cowboy hat', 'panama hat', 'graduate hat', 'white basecap', 'gold basecap',
                        'green basecap', 'blue basecap', 'black basecap', 'red basecap', 'orange basecap',
                        'pink basecap', 'blue forward cap', 'grey forward cap', 'maga cap', 'christmas hat',
                        'cat on head', 'tophat', 'sombrero', 'sun hat', 'pirate hat', 'rasta hat', 'nurse hat',
                        'viking helmet', 'safety helmet', 'tinfoil hat', 'default hat'],
                'glasses': ['violet shades', 'black shades', 'white glasses', 'gold glasses', 'blue glasses',
                            'green glasses', 'pink glasses', 'orange glasses', 'red glasses', 'black glasses',
                            'mirror glasses', 'nerd glasses', 'default glasses'],
                'accessories': ['chicken', 'parrot', 'black bandana', 'red bandana', 'blue bandana', 'pipe', 'cigar',
                                'cigarette', 'violet-yellow headband', 'red-white headband', 'face mask', 'eye mask',
                                'eye patch', 'black braces', 'white braces', 'red braces', 'red scarf', 'black scarf',
                                'white scarf', 'white parisian scarf', 'black parisian scarf', 'red parisian scarf',
                                'chain with clock', 'chain with cross upside down', 'chain with cross',
                                'blue messy tie', 'black messy tie', 'red messy tie', 'red tie', 'black tie',
                                'blue tie', 'golden key chain', 'silver key chain', 'boxing belt', 'leather belt',
                                'gold chain', 'rings', 'bracelet right arm', 'bracelet left arm', 'handcuffs',
                                'gloves', 'default accessories'],
                'top': ['undershirt', 'dirty undershirt', 'bloody undershirt', 'white muscle shirt',
                        'pink rainbow shirt', 'white rainbow shirt', 'black rainbow shirt', 'grey muscle shirt',
                        'blue-white sport shirt', 'yellow-black sport shirt', 'violet-yellow sport shirt',
                        'red sport shirt', 'gold cape', 'blue cape', 'white cape', 'green cape', 'red cape',
                        'green bra', 'gold bra', 'pink bra', 'black bra', 'red bra', 'spido shirt',
                        'red spaghetti top', 'green spaghetti top', 'black belly free shirt',
                        'white belly free shirt', 'police uniform', 'red-white striped shirt',
                        'blue-white striped shirt', 'open black shirt', 'open blue shirt', 'open green shirt',
                        'open violet shirt', 'open yellow shirt', 'open pink shirt', 'open white shirt',
                        'bellboy jacket', 'white nipple free shirt', 'pink nipple free shirt',
                        'blue nipple free shirt', 'open black shirt with red knobs', 'open grey shirt', 'nurse shirt',
                        'white heart shirt', 'yellow heart shirt', 'black bitcoin shirt', 'red bitcoin shirt',
                        'white shirt', 'vertical striped blue-white shirt', 'vertical striped yellow-white shirt',
                        'vertical striped red-white shirt', 'grey shirt', 'orange prison shirt',
                        'black-white prison shirt', 'open camouflage shirt', 'camouflage longsleeve',
                        'longsleeve with red stripes', 'green bulletproof vest', 'dark bulletproof vest',
                        'felt jacket', 'blue jacket', 'plaid jacket', 'black jacket with blue shirt', 'green jacket',
                        'yellow jacket', 'violet jacket', 'red jacket', 'black jacket', 'colorful longsleeve',
                        'colorful longsleeve with dark background', 'anchor longsleeve', 'black longsleeve with skull',
                        'white longsleeve with skull', 'pink longsleeve', 'black longsleeve with alien',
                        'white longsleeve', 'green longsleeve', 'yellow longsleeve with smile', 'yellow longsleeve',
                        'red longsleeve', 'black longsleeve', 'blue longsleeve', 'safety vest', 'default top'],
                'bottom': ['black socks', 'white socks', 'yellow-white socks', 'green-white socks', 'blue-white socks',
                           'red-white socks', 'pink socks', 'red overknee socks', 'diaper', 'pissed white pants',
                           'plaid boxer shorts', 'red-black boxer shorts', 'striped boxer shorts', 'grey boxer shorts',
                           'pink string', 'green string', 'red string', 'blue string', 'gold string', 'black string',
                           'white string', 'red hot pants', 'black fishnet', 'red fishnet', 'red sport shorts',
                           'violet-yellow sport shorts', 'spido pants', 'split pants', 'blue shorts', 'green shorts',
                           'white shorts', 'yellow shorts', 'pink shorts', 'black shorts', 'white pants',
                           'plaid black-white pants', 'plaid black-red pants', 'black-white prison pants',
                           'orange prison pants', 'blue jeans', 'plaid red-white shorts', 'plaid black-white shorts',
                           'plaid red-black shorts', 'plaid green-black shorts', 'camouflage pants', 'beige pants',
                           'blue pants', 'pink pants', 'brown pants', 'black pants', 'yellow pants', 'green pants',
                           'red pants', 'default bottom'],
                'body': ['cyborg', 'silver eyebrow piercing left', 'silver eyebrow piercing right',
                         'golden eyebrow piercing right', 'golden eyebrow piercing left', 'silver stud earring right',
                         'silver stud earring left', 'large earring left', 'large earring right',
                         'golden stud earring right', 'golden stud earring left', 'belly button piercing',
                         'nipple piercing', 'nipple chain', 'silver nosering', 'golden nosering', 'gouged eye left',
                         'gouged eye right', 'blue eye left', 'blue eye right', 'shoulder scar', 'face scar',
                         'belly scar', 'arm scar', 'tattoos on left leg', 'tattoos on right leg', 'tattoos on left arm',
                         'tattoos on right arm', 'skull tattoo black', 'skull tattoo black-white', 'heart tattoo',
                         'bitcoin tattoo', 'rainbow tattoo', 'silver genital piercing', 'golden genital piercing',
                         'body hair', 'pimples', 'default body'],
                'hair': ['fringe black', 'fringe brown', 'fringe grey', 'fringe red', 'fringe blonde',
                         'light brown residual hair', 'red residual hair', 'grey residual hair',
                         'blonde residual hair', 'black horseshoe hairline', 'light brown horseshoe hairline',
                         'red horseshoe hairline', 'grey horseshoe hairline', 'blonde horseshoe hairline',
                         'red blowout', 'light brown blowout', 'black blowout', 'grey blowout', 'blonde blowout',
                         'long curls grey', 'long curls red', 'long curls black', 'long curls light brown',
                         'long curls blonde', 'red stubbles', 'blonde stubbles', 'black stubbles', 'black sidecut',
                         'light brown sidecut', 'red sidecut', 'grey sidecut', 'blonde sidecut', 'double mohawk',
                         'blonde mohawk', 'black mohawk', 'red mohawk', 'blue mohawk', 'green mohawk', 'red buzzcut',
                         'black buzzcut', 'brown buzzcut', 'blonde buzzcut', 'dark brown bowl', 'light brown bowl',
                         'grey bowl', 'black bowl', 'red bowl', 'blonde bowl', 'wild grey hair', 'wild orange hair',
                         'wild pink hair', 'wild black hair', 'wild blue hair', 'wild red hair', 'wild green hair',
                         'wild dark brown hair', 'wild light brown hair', 'wild blonde hair', 'flat top red',
                         'flat top black', 'flat top blonde', 'flat top light brown', 'flat top grey',
                         'straight long black hair', 'straight long light brown hair', 'straight long red hair',
                         'straight long grey hair', 'straight long blonde hair', 'pigtail', 'grey messy hair',
                         'red messy hair', 'light brown messy hair', 'black messy hair', 'blonde messy hair',
                         'short brown fringe', 'short red fringe', 'short light brown fringe', 'short black fringe',
                         'short blonde fringe', 'sharp dark brown flattop', 'sharp light brown flattop',
                         'sharp black flattop', 'sharp red flattop', 'sharp blonde flattop',
                         'shoulder-length orange hair', 'shoulder-length pink hair', 'shoulder-length black hair',
                         'shoulder-length blue hair', 'shoulder-length green hair', 'shoulder-length red hair',
                         'shoulder-length dark brown hair', 'shoulder-length light brown hair',
                         'shoulder-length blonde hair', 'dark brown pompadour', 'red pompadour', 'black pompadour',
                         'light brown pompadour', 'blonde pompadour', 'default hair'],
                'mouth': ['wide mouth with missing teeth', 'wide mouth with gold teeth',
                          'wide mouth with missing incisors', 'wide mouth with one teeth', 'wide mouth', 'quiet smile',
                          'smile', 'sad mouth', 'sceptical mouth', 'staggered mouth with gold teeth',
                          'staggered mouth with black teeth', 'staggered mouth', 'default mouth'],
                'beard': ['long red beard', 'long black beard', 'long light brown beard', 'long brown beard',
                          'long grey beard', 'long blonde beard', 'blonde beard', 'grey beard', 'brown beard',
                          'red beard', 'light brown beard', 'red goatee', 'light brown goatee', 'blonde goatee',
                          'grey goatee', 'brown goatee', 'van dyke red', 'van dyke blonde', 'van dyke grey',
                          'van dyke light brown', 'van dyke brown', 'red zappa beard', 'blonde zappa beard',
                          'grey zappa beard', 'light brown zappa beard', 'brown zappa beard', 'red dali beard',
                          'blonde dali beard', 'grey dali beard', 'light brown dali beard', 'brown dali beard',
                          'brown handlebar', 'light brown handlebar', 'grey handlebar', 'red handlebar',
                          'blonde handlebar', 'grey mustache', 'red mustache', 'blonde mustache',
                          'light brown mustache', 'brown mustache', 'petite goatee light brown', 'petite goatee red',
                          'petite goatee grey', 'petite goatee brown', 'petite goatee blonde', 'red extended handlebar',
                          'grey extended handlebar', 'light brown extended handlebar', 'blonde extended handlebar',
                          'grey mutton chops', 'light brown mutton chops', 'red mutton chops', 'brown mutton chops',
                          'blonde mutton chops', 'light brown chin strap', 'grey chin strap', 'red chin strap',
                          'blonde chin strap', 'light brown dutch beard', 'red dutch beard', 'grey dutch beard',
                          'blonde dutch beard', 'brown dutch beard', 'default beard'],
                'eyes': ['white eyes', 'grey eyes', 'brown eyes', 'green eyes', 'red eyes', 'blue eyes',
                         'default eyes'],
                'skin': ['white skin with penis', 'white skin without genitals', 'white skin with vagina',
                         'zombie with penis', 'zombie without genitals', 'zombie with vagina',
                         'dark brown skin with penis', 'dark brown skin with vagina',
                         'dark brown skin without genitals', 'piggy skin with vagina',
                         'piggy skin without genitals', 'piggy skin with penis', 'ape with vagina',
                         'ape without genitals', 'ape with penis', 'brown with penis', 'brown with vagina',
                         'brown without genitals']
                }
trait_categories = list(trait_groups.keys())

# Initialize the max number of traits found for a category.
trait_len = {}
category_count_dict = {}
for key in trait_categories:
    trait_len[key] = 0
    category_count_dict[key] = {}

# Initialize the skills.
skills_categories = ['niftiness', 'power', 'swag', 'wealth', 'empathy', 'health']
skills_list = ['ultimate', 'legendary', 'gold', 'silver', 'ordinary']
skills_dict = {}
for key in skills_list:
    skills_dict[key] = {'name': key,
                        'count': 0,
                        'rarity': 0}

w3 = web3.Web3(web3.HTTPProvider(infura_url))

print(w3.isConnected())

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Get the supply.
total_supply = contract.functions.totalSupply().call()

# Read the trait numbers.
traits_dict = {}
traits_translator = {}
with open(traits_file, 'r') as traits_file_obj:
    raw_traits_data = traits_file_obj.readlines()
    for i_trait, line in enumerate(raw_traits_data):
        traits_translator[100+i_trait] = line.strip()
        traits_dict[line.strip()] = {'id': 100+i_trait,
                                     'name': line.strip(),
                                     'count': 0,
                                     'rarity': 0}

for i_c, category in enumerate(trait_categories):
    traits_dict[f"default {category}"] = {'id': i_c+1,
                                          'name': f"default {category}",
                                          'count': 0,
                                          'rarity': 0}

# Extract the token data.
token_data = {}
for i_token in range(total_supply):
    # Pull the traits.
    traits = str(contract.functions.getTraits(i_token+1).call())
    token_traits = [int(traits[i:i+3]) for i in range(0, len(traits), 3)]
    token_trait_names = [traits_translator[t_id] for t_id in token_traits]

    # Pull the skills.
    skills = contract.functions.getSkills(i_token+1).call()
    skill_total = sum(skills)

    # Create the dict for each token.
    token_data[i_token] = {'traits_ids': token_traits,
                           'trait_names': token_trait_names,
                           'skill_values': skills,
                           'total_skills': skill_total}
    for key in trait_categories:
        token_data[i_token][key] = []

    # Place the token's traits in each category.
    for trait in token_traits:
        name = traits_translator[trait]
        # Add categorized names.
        for category in trait_categories:
            if name in trait_groups[category]:
                token_data[i_token][category].append(name)

        # Count trait occurrences.
        traits_dict[name]['count'] += 1

    # Log empty categories.
    for category in trait_categories:
        if not token_data[i_token][category]:
            token_data[i_token][category].append(f"default {category}")
            traits_dict[f"default {category}"]['count'] += 1

    # Count the number of traits in a category.
    for category in trait_categories:
        count_name = f"{len(token_data[i_token][category])} Traits"
        if count_name not in category_count_dict[category].keys():
            category_count_dict[category][count_name] = {'count': 1,
                                                         'rarity': 0}
        else:
            category_count_dict[category][count_name]['count'] += 1

    # Check to see if the max trait length should be updated. Finds the max number of layers for a category.
    for category in trait_categories:
        if len(token_data[i_token][category]) > trait_len[category]:
            trait_len[category] = len(token_data[i_token][category])

    # Assign the skill values.
    for i_s, skill in enumerate(skills_categories):
        token_data[i_token][skill] = skills[i_s]

    # Assign the skill type.
    if skill_total >= 600:
        token_data[i_token]['skill_type'] = 'ultimate'
        skills_dict['ultimate']['count'] += 1
    elif skill_total >= 500:
        token_data[i_token]['skill_type'] = 'legendary'
        skills_dict['legendary']['count'] += 1
    elif skill_total >= 400:
        token_data[i_token]['skill_type'] = 'gold'
        skills_dict['gold']['count'] += 1
    elif skill_total >= 300:
        token_data[i_token]['skill_type'] = 'silver'
        skills_dict['silver']['count'] += 1
    else:
        token_data[i_token]['skill_type'] = 'ordinary'
        skills_dict['ordinary']['count'] += 1

# Write the token data to a json.
with open('tokens.json', 'w') as token_file_obj:
    json.dump(token_data, token_file_obj)

# Calculate rarity of each trait.
single_traits = []
for key in traits_dict.keys():
    traits_dict[key]['rarity'] = traits_dict[key]['count'] / total_supply
    if traits_dict[key]['count'] == 1:
        single_traits.append(key)

# Pull out the single trait tokens.
token_single = {}
single = 0
for token in token_data.keys():
    for category in trait_categories:
        for trait in token_data[token][category]:
            if trait in single_traits:
                token_single[single] = {'Token ID': token+1,
                                        'Category': category,
                                        'Trait': trait}
                single += 1

# Calculate rarity of each skill.
for key in skills_dict.keys():
    skills_dict[key]['rarity'] = skills_dict[key]['count'] / total_supply

# Calculate rarity of each category.
for category in trait_categories:
    for key in category_count_dict[category]:
        category_count_dict[category][key]['rarity'] = category_count_dict[category][key]['count'] / total_supply

# Write the single trait list.
with open('single_trait.csv', 'w', newline='') as single_file_obj:
    csv_writer = csv.DictWriter(single_file_obj, fieldnames=['Token ID', 'Category', 'Trait'])
    csv_writer.writeheader()
    for key in token_single.keys():
        csv_writer.writerow(token_single[key])

# Write the rarity list.
with open('trait_rarity.csv', 'w', newline='') as trait_rarity_file_obj:
    csv_writer = csv.DictWriter(trait_rarity_file_obj, fieldnames=['id', 'name', 'count', 'rarity'])
    csv_writer.writeheader()
    for key in traits_dict.keys():
        csv_writer.writerow(traits_dict[key])

# Write the skills list.
with open('skills_rarity.csv', 'w', newline='') as skills_rarity_file_obj:
    csv_writer = csv.DictWriter(skills_rarity_file_obj, fieldnames=['name', 'count', 'rarity'])
    csv_writer.writeheader()
    for key in skills_dict.keys():
        csv_writer.writerow(skills_dict[key])

# Write the category count list.
with open('category_count.csv', 'w', newline='') as category_count_file_obj:
    csv_writer = csv.writer(category_count_file_obj)
    csv_writer.writerow(['Category', '# of Traits', 'Token Count', 'Rarity'])
    for category in trait_categories:
        for key in category_count_dict[category]:
            csv_writer.writerow([category, key, category_count_dict[category][key]['count'],
                                 category_count_dict[category][key]['rarity']])

# Token rarity.
token_rarity_dict = {}
for token in token_data.keys():
    token_rarity_dict[token] = {'Token ID': token+1
                                }
    for category in trait_categories:
        min_rarity = min([traits_dict[trait]['rarity'] for trait in token_data[token][category]])
        weighted_rarity = min_rarity * \
                          category_count_dict[category][f"{len(token_data[token][category])} Traits"]['rarity']
        token_rarity_dict[token][f"{category.capitalize()} Rarity (min)"] = min_rarity
        token_rarity_dict[token][f"{category.capitalize()} Rarity (avg)"] = sum([traits_dict[trait]['rarity']
                                                               for trait in token_data[token][category]]) / \
                                                          float(len(token_data[token][category]))
        token_rarity_dict[token][f"{category.capitalize()} Rarity (weighted)"] = weighted_rarity
        if category in ['top', 'bottom', 'accessories', 'body']:
            token_rarity_dict[token][f"# of {category.capitalize()}s"] = len(token_data[token][category])

    for skill, val in zip(skills_categories, token_data[token]['skill_values']):
        token_rarity_dict[token][skill.capitalize()] = val
    token_rarity_dict[token]['Total Skills'] = token_data[token]['total_skills']
    token_rarity_dict[token]['Skill Tier'] = token_data[token]['skill_type']
    token_rarity_dict[token]['Skill Rarity'] = skills_dict[token_data[token]['skill_type']]['rarity']

    total_rarity_min = np.prod([token_rarity_dict[token][f"{c.capitalize()} Rarity (min)"] for c in trait_categories] +
                               [token_rarity_dict[token]['Skill Rarity']])
    total_rarity_avg = np.prod([token_rarity_dict[token][f"{c.capitalize()} Rarity (avg)"] for c in trait_categories] +
                               [token_rarity_dict[token]['Skill Rarity']])
    total_rarity_weight = np.prod([token_rarity_dict[token][f"{c.capitalize()} Rarity (weighted)"]
                                   for c in trait_categories] + [token_rarity_dict[token]['Skill Rarity']])
    token_rarity_dict[token]['Rarity (min)'] = total_rarity_min
    token_rarity_dict[token]['Rarity (avg)'] = total_rarity_avg
    token_rarity_dict[token]['Rarity (weighted)'] = total_rarity_weight

# Write the token rarity data.
with open('token_rarity.csv', 'w', newline='') as token_rarity_file_obj:
    rarity_header = list(token_rarity_dict[list(token_rarity_dict.keys())[0]].keys())
    csv_writer = csv.DictWriter(token_rarity_file_obj, fieldnames=rarity_header)
    csv_writer.writeheader()
    for key in token_rarity_dict.keys():
        csv_writer.writerow(token_rarity_dict[key])
