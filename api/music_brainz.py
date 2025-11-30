from io import BytesIO
from PIL import Image
from requests import get as rget

class MusicBrainzAPI:
    """Access the MusicBrainz API (https://musicbrainz.org)"""
    
    __root_url = "https://musicbrainz.org/ws/2"

    def search_releases(self, title):
        results = self._search(title, "release")
        results = results["releases"]
        releases = [self._parse_release(r) for r in results]
        return releases
 
    
    def lookup_release(self, release_mbid):
        output = self._lookup(release_mbid, "release")
        release = self._parse_release(output)
        try:
            release["recordings"] = [
                {
                    "title" : track["title"],
                    "length" : track["length"]
                }
                for track in output["media"][0]["tracks"]
            ]
        except BaseException:
            pass
        return release


    def get_cover_art_data(self, release_mbid):
        try:
            url = f"https://coverartarchive.org/release/{release_mbid}"
            response = rget(url)
            response.raise_for_status()
            try: response = response.json()["images"][0]
            except: raise BaseException("Can't retrieve image")
            img_url = response["image"]
            img_response = rget(img_url)
            img_data = BytesIO(img_response.content)
            return img_data
        except:
            return None


    def _search(self, query, type):
        url = f"{self.__root_url}/{type}?query={query}&fmt=json"
        response = rget(url).json()
        return response
    

    def _lookup(self, mbid, type):
        url= f"{self.__root_url}/{type}/{mbid}?inc=recordings+artist-credits&fmt=json"
        response = rget(url).json()
        return response

    
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