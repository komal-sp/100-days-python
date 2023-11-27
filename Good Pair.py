A = [2, 1, 6, 4]


def solve(A):
    global oddsum
    pf_even = []
    s_e = 0
    N = len(A)
    for i in range(N):
        if i % 2 == 0:
            s_e += A[i]
            pf_even.append(s_e)
        else:
            pf_even.append(s_e)

    s_o = 0
    pf_odd = []
    for k in range(N):
        if k % 2 != 0:
            s_o += A[k]
            pf_odd.append(s_o)
        else:
            pf_odd.append(s_o)

        special = 0
        for j in range(N):
            if j > 0:
                evensum = pf_even[j - 1] + (pf_odd[N - 1] - pf_odd[j])
                oddsum = pf_odd[j - 1] + (pf_even[N - 1] - pf_odd[j])
            elif j == 0:
                evensum = pf_odd[N - 1] - pf_odd[j]
                oddsum = pf_even[N - 1] - pf_odd[j]

            if evensum == oddsum:
                special += 1

        print(special)

