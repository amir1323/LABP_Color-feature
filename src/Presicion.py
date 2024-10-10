import numpy as np

def extended_canberra_distance(T, Q):
    Ut = np.mean(T)
    Uq = np.mean(Q)
    return np.sum(np.abs(T - Q) / (np.abs(T + Ut) + np.abs(Q + Uq)))

def canberra_distance(T, Q):
    denominator = np.abs(T) + np.abs(Q)
    mask = denominator != 0
    D = np.sum(np.where(mask, np.abs(T - Q) / denominator, 0))
    return D

def square_chord_distance(T, Q):
    D = np.sum((np.sqrt(T) - np.sqrt(Q)) ** 2)
    return D

def chi_square_distance(T, Q):
    denominator = T + Q
    mask = denominator != 0
    D = np.sum(np.where(mask, ((T - Q) ** 2) / denominator, 0))
    return D

def euclidean_distance(T, Q):
    return np.sqrt(np.sum((T - Q) ** 2))

total_hist = np.load("data location")
num_categories = 10
elements_per_category = len(total_hist) // num_categories
for N in range(10,110,10):
        for cotte in range(0,1000,1000):
            low = cotte
            high = cotte + 100
            presg_tot = []
            for i in range(0, 1000):
                # print(i)
                T = total_hist[i]
                all_dis = np.zeros(len(total_hist), dtype='float32')
                for j in range(1000):
                    if i != j:
                        Q = total_hist[j]
                        all_dis[j] = chi_square_distance(T, Q)
                    else:
                        all_dis[j] = np.inf
                mins_argo = np.argpartition(all_dis, N)[:N] // elements_per_category
                same_category = np.sum(mins_argo == i // elements_per_category)
                presg_tot.append(same_category / N)

            print(f'extended canberra in {cotte} for N = {N} is equal to Precision : ', np.mean(np.array(presg_tot)) * 100)
            print(f'extended canberra in {cotte} for N = {N} is equal to Recall : ',( (np.mean(np.array(presg_tot)) ) * N) /100 )

