from requests import get as rget

class MusicBrainzAPI:
    """Access the MusicBrainz API (https://musicbrainz.org)"""
    
    __root_url = "https://musicbrainz.org/ws/2"


    def search_tracks(self, title):
        results = self._search(title, "recording")
        results = results["recordings"]
        tracks = [self._parse_track(r) for r in results]
        return tracks
    
    def search_releases(self, title):
        results = self._search(title, "release")
        results = results["releases"]
        releases = [self._parse_release(r) for r in results]
        return releases

    def _search(self, query, type):
        url = f"{self.__root_url}/{type}?query={query}&fmt=json"
        response = rget(url).json()
        return response

  
    def _parse_track(self, track: dict):
        out = {
            "id" : track["id"],
            "title" : track["title"],
            "artists" : track["artist-credit"] if "artist-credit" in track else [],
            "release_date" : track["first-release-date"] if "first-release-date" in track else "No date"
        }

        if len(out["artists"]) > 0:
            a = []
            for artist in out["artists"]:
                a.append(artist["name"])
            out["artists"] = a

        return out
    
    def _parse_release(self, release: dict):
        out = {
            "id" : release["id"],
            "title" : release["title"],
            "artists" : release["artist-credit"] if "artist-credit" in release else [],
            "release_date" : release["date"] if "date" in release else "No date"
        }

        if len(out["artists"]) > 0:
            a = []
            for artist in out["artists"]:
                a.append(artist["name"])
            out["artists"] = a

        return out