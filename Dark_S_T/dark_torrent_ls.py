import dataclasses
from types import MappingProxyType

@dataclasses.dataclass()
class lks():
    M_URL: str
    R_URL: str
    S_URL: str

    def __post_init__(self):
        thurls = [self.M_URL, self.R_URL, self.S_URL]
        for the in thurls:
            if not str(the).startswith("http"):
                self.M_URL = ""
                self.R_URL = ""
                self.S_URL = ""


the_urls = MappingProxyType({'XUN234DSF': lks(
    'https://cdn.1337x.to/cdnsuggest.php?term=',
    'https://1337x.unblockit.ink/',
    'https://1337x.unblockit.ink/search/'
).__dict__})