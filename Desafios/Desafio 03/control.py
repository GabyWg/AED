import soporte as sp

def view_repeat(vector):
    cod =  []
    freq = []
    for i in range(len(vector)):
        flg = True
        for j in range(max(1,len(cod))):
            if len(cod) == 0:
                cod.append(vector[i])
                freq.append(1)
                flg = False
            elif vector[i] == cod[j]:
                freq[j] += 1
                flg = False
                break
        if flg:
            cod.append(vector[i])
            freq.append(1)
            
    return cod,freq

def modal_value(cod,freq):
    max_value_mod = 0
    ind_value_mod = 0

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
    vec = sp.vector_unknown_range(n)
    
    code,frequency= view_repeat(vec)

    ind_moda_num = modal_value(code,frequency)

    print(f"Numeros diferentes: {len(code)}")
    print(f"Value Number Modal: {(code[ind_moda_num])} - Frequency: {(frequency[ind_moda_num])}")

if __name__ == "__main__":
    principal()
