
# string = "It is a herbaceous perennial which produces flowers in the typical aroid structure: a densely crowded inflorescence called a spadix is subtended by one large bract called a spathe (occasionally two spathes are produced, with the upper spathe smaller). The spadix is generally cream or ivory when young, and turns green with age; the spathe is generally white or white with green nerves distally from the margin, turning green with age. Leaves are basal, glossy and somewhat deeply veined, ovate and acuminate. The petioles are long and the leaves arch gracefully. The plant produces offsets at the base and in time becomes a dense clump. Spathiphyllum wallisii is one of approximately 40 species in a genus of tropical evergreens. It was discovered in the late 19th century growing wild in Colombia. A number of cultivars, many of hybrid origin, are commercially available, such as the larger hybrids \"Mauna Loa\", named after the Hawaiian volcano, and the even larger “Sensation\", which are both popular indoor plants. \"Domino\" is a finely variegated variety of intermediate size. Its wide natural range includes parts of Mexico, the Caribbean Islands, and northern South America."
string = input()

string = string.replace('!', '').replace(',', '').replace('.', '').replace('?', '')
string = string.replace(';', '').replace(':', '').replace('#', '').replace('$', '')
string = string.replace('%', '').replace('^', '').replace('&', '').replace('*', '')
string = string.replace('(', '').replace(')', '').lower()
# !,.?;:#$%^&*(),

new_string = sorted(string.split(' '))

d_string = {x : new_string.count(x) for x in new_string}
# print(d_string.items())

for key, value in d_string.items():
    if value > 2 and len(key) > 4 and len(set(key)) > 3:
        print(key)