
import requests

if __name__ == "__main__":

    url = "https://pokeapi.co/api/v2/pokemon/{}"
    pokemon = input("Informe o nome de um Pokémon: ").lower()

    try:
        response = requests.get(
            url.format(pokemon)
        )

        if response.status_code == 200:
            pokemon_data = response.json()

            pokemon_id = pokemon_data.get("id")
            pokemon_name = pokemon_data.get("name")
            pokemon_height = pokemon_data.get("height")
            pokemon_weight = pokemon_data.get("weight")

            pokemon_types = []

            for pokemon_type in pokemon_data.get("types"):
                pokemon_types.append(pokemon_type.get("type").get("name"))


            print(f"Nome: {pokemon_name}")
            print(f"ID: {pokemon_id}")
            print(f"Altura: {pokemon_height}")
            print(f"Peso: {pokemon_weight}")
            print(f"Tipos: {pokemon_types}")

        else:
            raise Exception(f"Código HTTP incorreto: {response.status_code}.")
        
    except Exception as exc_info:
        print(f"Erro: {exc_info}")