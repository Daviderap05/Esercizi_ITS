import re

def text_analysis(paragraph: str) -> None:
    
    occurrences: dict[str, int] = {}
    word: str = ""
    
    words: list[str] = re.findall(r'\b\w+\b', paragraph.lower())
    
    for word in words:
           
        if word not in occurrences:
            
            occurrences[word] = 1
            
        else:
            
            occurrences[word] += 1

    print(dict(sorted(occurrences.items(), key=lambda item: item[1], reverse=True)))


            
p: str = "nel nel ciao ciao ciao a 9... ma p"  
text_analysis(p)