def mutate_string(string, position, character):
    rcv=string[:position]+character+string[position+1:]
    return rcv