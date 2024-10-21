from tqdm import tqdm
from colorama import Fore, init

init(autoreset=True)

def greet(name):    
    return f"Hello, {name}!"

def main():
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]    
    for name in tqdm(names, desc="Greeting names", unit="person"):
        greeting = greet(name)
        print(f"{Fore.GREEN}{greeting}")

if __name__ == "__main__":
    main()