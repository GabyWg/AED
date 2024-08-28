import soporte as sp

def view_repeat(vector,n):
    freq =  [0]*n
    repeat_num = 0
    for i in range(len(vector)):
        freq[vector[i]] +=1
    
    for i in freq:
        if i != 0:
            repeat_num += 1

    return freq,repeat_num

def modal_value(freq):
    max_value_mod = 0
    count_value_mod = 0

    print (max(freq))
    for i in range(len(freq)):
        if max_value_mod == freq[i]:
            count_value_mod += 1
        if freq[i] > max_value_mod:
            max_value_mod = freq[i]
            ind_value_mod = i
            count_value_mod = 1

    print(max_value_mod,"-",ind_value_mod,"-",count_value_mod)

    return ind_value_mod if count_value_mod == 1 else 0
def principal():
    
    n = 300000
    vec = sp.vector_known_range(n)

    frequency,num_repeat= view_repeat(vec,n)

    ind_moda_num = modal_value(frequency)

    print(f"Numeros diferentes: {num_repeat}")
    print(f"Value Number Modal: {ind_moda_num} - Frequency: {(frequency[ind_moda_num])}")

if __name__ == "__main__":
    principal()
