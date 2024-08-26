d_in = input().split()
towns = [d_in[i] for i in range(len(d_in)) if i % 2 == 0]
peoples = [int(d_in[i]) for i in range(len(d_in)) if i % 2 != 0]

res = [[towns[i], peoples[i]] for i in range(len(towns))]