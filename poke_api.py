import requests
import re

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    poke_info = get_pokemon_info("Rockruff")
    if poke_info:
        print(poke_info)
    else:
        print("Failed to get the Pokémon information.")

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokémon from the PokeAPI.

    Args:
        pokemon_name (str): Pokémon name (or PokéDex number)

    Returns:
        dict: Dictionary of Pokémon information, if successful. Otherwise, None.
    """

    def clean_pokemon_name(name):
        name = name.strip()
        name = name.lower()
        name = re.sub(r'[^a-zA-Z0-9\s\-]', '', name)
        name = name.replace(' ', '-')
        return name
    
    cleaned_name = clean_pokemon_name(pokemon_name)
    url = f'{POKE_API_URL}{cleaned_name}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Fetching data for Pokémon: {cleaned_name}")
        pokemon_data = response.json()
        return pokemon_data
    
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == '__main__':
    main()
