def replacer(str,items,repl):
    x = "".join(map(lambda x:repl if x in items else x,str))
    return x

