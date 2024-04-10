from dotenv import load_dotenv, find_dotenv
import json
import os
from openai import OpenAI
#from openai.embeddings_utils import get_embedding, cosine_similarity
import numpy as np

_ = load_dotenv('openAI.env')
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get('openAI_api_key'),
)

with open('movie_descriptions.json', 'r') as file:
    file_content = file.read()
    movies = json.loads(file_content)

#Esta función devuelve una representación numérica (embedding) de un texto, en este caso
#la descripción de las películas
    
def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

emb = get_embedding(movies[7]['description'])
print(emb)

#Vamos a crear una nueva llave con el embedding de la descripción de cada película en el archivo .json


for i in range(len(movies)):
#for i in range(6):
  emb = get_embedding(movies[i]['description'])
  movies[i]['embedding'] = emb


#Vamos a almacenar esta información en un nuevo archivo .json
file_name = 'movie_descriptions_embeddings.json'
with open(file_name, 'w') as file:
    json.dump(movies, file)


print(movies[0])

#Para saber cuáles películas se parecen más, podemos hacer lo siguiente:
print(movies[27]['title'])
print(movies[3]['title'])
print(movies[20]['title'])

#Calculamos la similitud de coseno entre los embeddings de las descripciones de las películas. Entre más alta la similitud
#más parecidas las películas.

print(f"Similitud entre película {movies[27]['title']} y {movies[3]['title']}: {cosine_similarity(movies[27]['embedding'],movies[3]['embedding'])}")
print(f"Similitud entre película {movies[27]['title']} y {movies[20]['title']}: {cosine_similarity(movies[27]['embedding'],movies[20]['embedding'])}")
print(f"Similitud entre película {movies[20]['title']} y {movies[3]['title']}: {cosine_similarity(movies[20]['embedding'],movies[3]['embedding'])}")

#Si se tuviera un prompt por ejemplo: Película de la segunda guerra mundial, podríamos generar el embedding del prompt y comparar contra 
#los embeddings de cada una de las películas de la base de datos. La película con la similitud más alta al prompt sería la película
#recomendada.

req = "super heroes"
emb = get_embedding(req)

sim = []
for i in range(len(movies)):
  sim.append(cosine_similarity(emb,movies[i]['embedding']))
sim = np.array(sim)
idx = np.argmax(sim)
print(movies[idx]['title'])


