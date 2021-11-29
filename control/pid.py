#!/usr/bin/env python3
#será considerado aqui que todo erro passado não é só igual, como unitário. Portanto, para 10 loops,
#teremos previsivelmente erro integral= 10, e erro derivativo = 29:
def calc_pid(kp,ki,kd,erro,erro_passado,n_loops):
    erro_int=0
    for i in range(n_loops):
        erro_int += erro_passado
    erro_der= n_loops - erro_passado
    pid= kp*erro + kd*(erro_der) + ki*(erro_int)
    return pid

resp= calc_pid(3,1,0.1,30,1,10)
print(resp)