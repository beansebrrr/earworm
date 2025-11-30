from requests import get as rget

class MusicBrainzAPI:
    """Access the MusicBrainz API (https://musicbrainz.org)"""
    
    __root_url = "https://musicbrainz.org/ws/2"


    def search_tracks(self, title):
        results = self._search(title, "recording")
        results = results["recordings"]
        tracks = [self._parse_track(r) for r in results]
        return tracks


    def _search(self, query, type):
        url = f"{self.__root_url}/{type}?query={query}&fmt=json"
        response = rget(url).json()
        return response

  
    def _parse_track(self, track: dict):
        out = {
            "id" : track["id"],
            "title" : track["title"],
            "artists" : track["artist-credit"] if "artist-credit" in track else [],
            "releases" : track["releases"] if "releases" in track else []
        }

        if len(out["artists"]) > 0:
            a = []
            for artist in out["artists"]:
                a.append(artist["name"])
                if "joinphrase" in artist: a.append(artist["joinphrase"])
            out["artists"] = "".join(a)

        if len(out["releases"]) > 0:
            r = []
            for release in out["releases"]:
                r.append({ "id":release["id"], "title":release["title"] })
            out["releases"] = r

        return out