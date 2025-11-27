for i in range(1,11):  
    
    with open(f"{i}.txt", "w") as f:
        f.write(f"This is file {i}.txt\n")