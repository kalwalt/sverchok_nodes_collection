#alpha masking script

def sv_main(base=[],alpha=[]):

    data = []
    out = []

    in_sockets = [
        ['s', 'base', base],
        ['s', 'alpha', alpha]] 

    out_sockets = [
        ['s','data', data]
    ]
    
    print('alpha values: {0}'.format(alpha))
    print('base values: {0}'.format(base))
   
    if alpha and alpha[0]:
        #out[alpha] = src_a+dst_a*(1-src_a) this is correct!
        #out = [(1.0-a)*b + a for a, b in zip(alpha[0][0], base[0][0])]
        #i did this before. But maybe this is correct?
        out = [(1.0-b)*a for a, b in zip(alpha[0][0], base[0][0])]
       
        data.append(out)
             
  

    return in_sockets, out_sockets
