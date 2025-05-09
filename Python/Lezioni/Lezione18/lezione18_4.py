def text_analysis(paragraph: str):
    
    occurrences: dict[str, int] = {}
    word: str = ""
    
    for c in paragraph:
        
        if c != " " or c != "," or c != ".":
            
            word += c.lower()
        
        else:
            
            if word not in occurrences:
                
                occurrences[word] = 1
                
            else:
                
                occurrences[word] += 1
        
    print(occurrences)
    
            
p: str = "Nel pattinaggio artistico su ghiaccio, nome di alcuni esercizi facenti parte delle 17 figure obbligatorie di scuola, che vengono eseguiti prima su uno e poi sull'altro piede, descrivendo un tracciato simile a due cerchi giustapposti."  
text_analysis(p)