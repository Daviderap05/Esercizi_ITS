import re
from re import Match    

class Anno:
    
    def __init__(self, anno: str):

        pre_check = re.fullmatch(r"^19\d\d$|2[0-1]\d\d$", anno)

        if pre_check is None:
            
            raise ValueError("Anno non valido, deve essere compreso tra 1900 e 2199")
        
        self.anno = pre_check.group(0)

    def __str__(self):
        
        return self.anno