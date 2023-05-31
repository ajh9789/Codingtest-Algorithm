def solution(code):
    mode=0
    ret=""
    for idx in range(len(code)):
        if(mode==0):
            if(not code[idx]=="1"):
                if(idx%2==0):
                    ret=ret+code[idx]
            else:
                if(code[idx]=="1"):
                    mode=1
        else:
            if(not code[idx]=="1"):
                if(idx%2==1):
                    ret=ret+code[idx]
            else:
                mode=0
    if(ret=="") :
        ret="EMPTY"
    return ret