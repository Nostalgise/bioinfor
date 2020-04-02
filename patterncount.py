def create_frequency_table(string,k):
    freqs={}
    for kmer in [string[i:i+k] for i in range(len(string)-k+1)]:
        print (kmer,i)
        if kmer in freqs:
            freqs[kmer]+=1
        else:
            freqs[kmer]=1
    return freqs


def find_most_frequent_words(string,k):
    most_frequent_words=[]
    max_k=-1
    for kmer,count in create_frequency_table(string,k).items():
        if count>max_k:
            max_k=count
            most_frequent_words=[]
        if count==max_k:
            most_frequent_words.append(kmer)
    return most_frequent_words

#print (find_most_frequent_words("CGATATATCCATAGTAT",3))

                
