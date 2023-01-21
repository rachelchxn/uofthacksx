import cohere
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

# have to put api key in .env
co = cohere.Client(os.getenv('API_KEY_COHERE'))

# wikipedia page for machine learning
prompt = f"""Passage: Is Wordle getting tougher to solve? Players seem to be convinced that the game has gotten harder in recent weeks ever since The New York Times bought it from developer Josh Wardle in late January. The Times has come forward and shared that this likely isn't the case. That said, the NYT did mess with the back end code a bit, removing some offensive and sexual language, as well as some obscure words There is a viral thread claiming that a confirmation bias was at play. One Twitter user went so far as to claim the game has gone to "the dusty section of the dictionary" to find its latest words.

TLDR: Wordle has not gotten more difficult to solve.
--
Passage: ArtificialIvan, a seven-year-old, London-based payment and expense management software company, has raised $190 million in Series C funding led by ARG Global, with participation from D9 Capital Group and Boulder Capital. Earlier backers also joined the round, including Hilton Group, Roxanne Capital, Paved Roads Ventures, Brook Partners, and Plato Capital.

TLDR: ArtificialIvan has raised $190 million in Series C funding.
--
Passage: The National Weather Service announced Tuesday that a freeze warning is in effect for the Bay Area, with freezing temperatures expected in these areas overnight. Temperatures could fall into the mid-20s to low 30s in some areas. In anticipation of the hard freeze, the weather service warns people to take action now.

TLDR:"""

prompt1 = f"""Christopher Columbus[a] (/kəˈlʌmbəs/;[3] born between 25 August and 31 October 1451, died 20 May 1506) was an Italian[b] explorer and navigator who completed four voyages across the Atlantic Ocean sponsored by the Catholic Monarchs of Spain, opening the way for the widespread European exploration and colonization of the Americas. His expeditions were the first known European contact with the Caribbean, Central America, and South America.

The name Christopher Columbus is the anglicisation of the Latin Christophorus Columbus. Scholars generally agree that Columbus was born in the Republic of Genoa and spoke a dialect of Ligurian as his first language. He went to sea at a young age and travelled widely, as far north as the British Isles and as far south as what is now Ghana. He married Portuguese noblewoman Filipa Moniz Perestrelo, who bore his son Diego, and was based in Lisbon for several years. He later took a Castilian mistress, Beatriz Enríquez de Arana, who bore his son, Fernando (also given as Hernando).[5][6][7]

Largely self-educated, Columbus was knowledgeable in geography, astronomy, and history. He developed a plan to seek a western sea passage to the East Indies, hoping to profit from the lucrative spice trade. After the Granada War, and following Columbus's persistent lobbying in multiple kingdoms, the Catholic Monarchs Queen Isabella I and King Ferdinand II agreed to sponsor a journey west. Columbus left Castile in August 1492 with three ships and made landfall in the Americas on 12 October, ending the period of human habitation in the Americas now referred to as the pre-Columbian era. His landing place was an island in the Bahamas, known by its native inhabitants as Guanahani. He subsequently visited the islands now known as Cuba and Hispaniola, establishing a colony in what is now Haiti. Columbus returned to Castile in early 1493, bringing a number of captured natives with him. Word of his voyage soon spread throughout Europe.

Columbus made three further voyages to the Americas, exploring the Lesser Antilles in 1493, Trinidad and the northern coast of South America in 1498, and the eastern coast of Central America in 1502. Many of the names he gave to geographical features, particularly islands, are still in use. He also gave the name indios ("Indians") to the indigenous peoples he encountered. The extent to which he was aware that the Americas were a wholly separate landmass is uncertain; he never clearly renounced his belief that he had reached the Far East. As a colonial governor, Columbus was accused by his contemporaries of significant brutality and was soon removed from the post. Columbus's strained relationship with the Crown of Castile and its appointed colonial administrators in America led to his arrest and removal from Hispaniola in 1500, and later to protracted litigation over the perquisites that he and his heirs claimed were owed to them by the crown.

Columbus's expeditions inaugurated a period of exploration, conquest, and colonization that lasted for centuries, thus bringing the Americas into the European sphere of influence. The transfer of commodities, ideas, and people between the Old World and New World that followed his first voyage are known as the Columbian exchange. Columbus was widely celebrated in the centuries after his death, but public perception has fractured in the 21st century as scholars have given greater attention to the harms committed under his governance, particularly the beginning of the depopulation of Hispaniola's indigenous Taínos caused by mistreatment and Old World diseases, as well as by that people's enslavement. Many places in the Western Hemisphere bear his name, including the country of Colombia, the District of Columbia, and British Columbia."""

def splitPrompt(prompt):
    a = iter(prompt.split('.'))
    map(".".join,zip(*[a]*3)) 
    return a

def getSummary(prompts):
    ret = []
    try:
        for prompt in prompts:
            prediction = co.generate(
                model='medium',
                prompt=prompt,
                max_tokens=20,
                num_generations=3,
                temperature=0.5,
                k=0,
                p=1,
                frequency_penalty=0,
                presence_penalty=0,
                return_likelihoods='GENERATION'
            )
            gens = []
            likelihoods = []
            for gen in prediction.generations:
                gens.append(gen.text)
                sum_likelihood = 0
                for t in gen.token_likelihoods:
                    sum_likelihood += t.likelihood
                # Get sum of likelihoods
                likelihoods.append(sum_likelihood)
            pd.options.display.max_colwidth = 200
            # Create a dataframe for the generated sentences and their likelihood scores
            df = pd.DataFrame({'generation':gens, 'likelihood': likelihoods})
            # Drop duplicates
            df = df.drop_duplicates(subset=['generation'])
            # Sort by highest sum likelihood
            df = df.sort_values('likelihood', ascending=False, ignore_index=True)
            ret.append(df.loc[0])
    except:
        print("error")
    return ret

a = sorted(getSummary(splitPrompt(prompt)), key=lambda x: x.likelihood)

#a is sorted by likelihood
for x in (a):
    print(x.generation)
    print('------------------')
    print('\n')
