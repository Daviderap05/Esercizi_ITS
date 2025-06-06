def make_shirt(size: str, text: str):
    
    print(f"\nThe shirt will be created with the phrase '{text}' and the size will be an {size}")

size2: str = input("Enter the size: ").lower()
text2: str = input("Enter the text: ")

make_shirt(size2, text2)

make_shirt(size = input("Enter the size: ").lower(), text = input("Enter the text: "))