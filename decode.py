def decode_options(opt):
    ret = ''
    for option in opt:
        if option[0] == 'MSS':
            ret += "M" + str(option[1])
        elif option[0] == 'WScale':
            ret += "W" + str(option[1])
        else:
            tmp = str(option[0])
            ret += tmp[0]
        ret += ','
    ret = ret[:-1]

    return(ret)