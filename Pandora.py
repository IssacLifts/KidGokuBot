
# Import again
import colorama
from requests import get


def aquire_uuid(username: str) -> dict:
    try:
        api_mojang = get(f"https://api.mojang.com/users/profiles/minecraft/%s" % (username))
    except ConnectionError:
        print(f"{colorama.Fore.RED}An error occured with your connection.\nAre you connected to the internet?\n")
        if __name__ == "__main__":
            return
        else:
            exit()
        
    if api_mojang.status_code != 200:
        print(f"{colorama.Fore.RED}'{username}' is not a valid user.")
        return 204

         
    return api_mojang.json()['id'] 

