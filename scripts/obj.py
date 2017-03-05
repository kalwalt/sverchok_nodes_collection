def sv_main(data=0.0):

    in_sockets = [
        ['o', 'obj', obj],
        ['s','float',data]
        ]

    out_sockets = [
    ['o','out',out]
    ]

    return in_sockets, out_sockets
