from api import MusicBrainzAPI
import json

def main():
    api = MusicBrainzAPI()
    _ = api.search_tracks("If the world was ending")[0:3]
    print(json.dumps(_, indent=2))


if __name__ == "__main__":
    main()
