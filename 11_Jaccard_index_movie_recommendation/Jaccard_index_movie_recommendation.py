import random
import itertools
import time


with open('tekst.txt', 'r') as file:
    content = file.read()
    
    
paragraphs = [paragraph.strip() for paragraph in content.split('\n\n') if paragraph.strip()]

def MinHash(paragraphs, seeds_number, plagiary_treshold, window_size):
    
    seeds = [random.getrandbits(64) for _ in range(seeds_number)]
    q = window_size
    
    #Start time
    start_time = time.time()

    par_hash_list = []
    for par in paragraphs:
        #Petla dla kazdego akapitu
        n = len(par)

        
        final_hash_list = []
        #Petla dla kazdego seeda
        for seed in seeds:
            i = 0
            hash_list = []
            #Okno przesuwne
            while i <n-15+1:
                okno = par[i:i+q]
                
                h = hash(okno) ^ seed
                #Okno przesuwne, na kazde okno jeden hash
                hash_list.append(h)
                i+=1
                
            #Min hash z tych utworzonych z okna przesuwnego    
            min_hash = min(hash_list)
            
            #Lista 100 hashy dla akapitu
            final_hash_list.append(min_hash)
            
        #Lista 100 hashy dla kazdego akapitu  
        par_hash_list.append(final_hash_list)
            
        
    
    
    n_parahraphs = len(par_hash_list)
    combinations = list(itertools.combinations(range(n_parahraphs), 2))
    for i, j in combinations:
        
        common = len(set(par_hash_list [i]) & set(par_hash_list [j]))
        
        if common >= plagiary_treshold:
            print(f"Akapity {paragraphs[i][0:13]}... i {paragraphs[j][0:13]}... są podobne (wspólnych hashy: {common})")    
        
        
    t = round(time.time() - start_time,4)
    print(f"Czas wykonania: {t} s") 
        
        
print("Parameters: seed_number = 100 ; treshold = 30 ; window_size = 15 ")    
MinHash(paragraphs, seeds_number = 100, plagiary_treshold = 30, window_size = 15)    

print("\n")

print("Parameters: seed_number = 10 ; treshold = 30 ; window_size = 15 ")    
MinHash(paragraphs, seeds_number = 10, plagiary_treshold = 30, window_size = 15)    

print("\n")

print("Parameters: seed_number = 50 ; treshold = 5 ; window_size = 15 ")    
MinHash(paragraphs, seeds_number = 50, plagiary_treshold = 5, window_size = 15)   

print("\n")

print("Parameters: seed_number = 100 ; treshold = 5 ; window_size = 5 ")    
MinHash(paragraphs, seeds_number = 100, plagiary_treshold = 5, window_size = 5)     
