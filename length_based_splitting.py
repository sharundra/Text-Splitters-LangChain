from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


text1 = """
Satyajit Ray: Cinematic Humanism from Pather Panchali to Shakha Prashakha

Born into a venerable Bengali artistic family and shaped by Tagore’s Santiniketan ideals, Satyajit Ray (1921–1992) carried in his heart a vision of India both intimate and universal
tcm.com
khabar.com
. His cinema, suffused with humanism and poetic realism, reaffirmed Bengali heritage within a modern context
tcm.com
. Ray did not graduate from film school – he was a graphic artist-turned-advertising designer who devoured Jean Renoir, Vittorio De Sica and Western literature – yet when he debuted with Pather Panchali (1955) he “created a new cinema for India”
rogerebert.com
. As Roger Ebert observed of the Apu Trilogy, its “great, sad, gentle sweep… creates a world so convincing that it becomes… another life we might have lived”
rogerebert.com
. This young director’s mastery of screenwriting, casting, editing and even musical scoring (he taught himself music and later composed many of his own scores) became legendary
tcm.com
khabar.com
. Indeed, Ray “taught himself music to write the score for his movies” after collaborating with Ravi Shankar early on
khabar.com
, and from 1961 onward was often the composer of his films
tcm.com
.

Ray’s cinema covered the sweep of Indian society with quiet depth. Beginning in a rural Bengal village, it moved through the zamindar mansions of Jalsaghar (1958), the urban middle-class of Mahanagar (1963), the educated elite of Nayak (1966) and Kanchenjungha (1962), the Marxist angst of the Calcutta Trilogy (1970–75), the rural Bengal famine in Ashani Sanket (1973), the patriotic ferment of Ghare Baire (1984), and even magical children’s tales and detective stories. Across these diverse settings, Ray’s camera showed ordinary people with extraordinary empathy. As one observer noted, his powerful images were a foundation for a sense of India – from “Apu and Durga in the kash grass” and the monsoon rains of Pather Panchali, to the chandeliers of Jalsaghar, to the stylish modern streets of Calcutta and the decaying mansions of Ghare Baire
openthemagazine.com
. This panoramic portrait of Indian life – its hopes, pains, traditions and changes – is a constant in Ray’s oeuvre.

The Apu Trilogy and the Rise of Realism (1955–1959)

Ray’s debut trilogy (Pather Panchali 1955, Aparajito 1956, Apur Sansar 1959) announced a new realism in Indian film. Shot on rural locations with largely amateur actors, the films depict Apu’s childhood and young manhood against poverty and social change. Ray’s storytelling is gentle yet profound, and he often filmed scenes with long takes, natural light and fluid camera movement. Cinematographer Subrata Mitra, once a still photographer, achieved effects of “extraordinary beauty” – forest paths, river vistas, gathering monsoon clouds – by balancing light and shadow with painterly precision
rogerebert.com
. Ebert describes a terrifying sequence of a mother watching her feverish daughter in a storm, where “we feel her fear… as the camera dollies again and again across the small, threatened space”
rogerebert.com
. Each shot in the trilogy unfolds with careful realism: characters “cast from life, to type,” in the words of Ebert, reflecting Ray’s debt to Italian neorealism
rogerebert.com
khabar.com
.

The effect was revolutionary: Pather Panchali (the “Song of the Road”) won international acclaim and funding (a historic state grant aided completion) and Aparajito took the Golden Lion at Venice. By 1959 the trilogy had “swept the top prizes at Cannes, Venice and London”
rogerebert.com
, firmly establishing Ray as a world-class filmmaker. Critics noted that Ray had “never before [seen] such a decisive impact on the films of his culture”
rogerebert.com
. He achieved this by a poetic use of detail and performance: Apu’s dreamy innocence, Durga’s lissome playfulness, the stoic wisdom in the mother Sarbajaya’s eyes. The Apu films unfold at an unhurried pace (“standing above fashion” as Ebert wrote)
rogerebert.com
, accumulating small moments – a cut fruit, a sparrow’s flight, a train whistle in the distance – until the emotional truths of these lives are laid bare.
"""

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0, separator = "")


documents = text_splitter.split_text(text1)
print(len(documents))
print(type(documents))
print(type(documents[0]))
print(len(documents[0]))

# #this next won't work as documents is a list of strings, so string doesn't have a page_content attribute
# print(documents[0].page_content)


loader = PyPDFLoader("Religion of India in 6th century BC (Part 1).pdf")
text2 = loader.load()
documents = text_splitter.split_documents(text2)

print(len(documents))
print(type(documents))
print(type(documents[0]))

## next line won't work because documents is a list of document obejct and not a string hence len() fucntion can't be applied on object.
# print(len(documents[0]))

print(documents[0])
print(f'printing only the page content part of the 1st document object : {documents[0].page_content}')
print(f'printing only the metadata part of the 1st document object : {documents[0].metadata}')