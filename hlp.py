def shfit (l :list ,  num : int) :
    """
    Function: shfit
    ---------------
    Performs a circular forward shift on a list of elements.
    Used in the ASENFA encryption process to shuffle digits in the key,
    adding an extra layer of randomness and obfuscation before encryption.

    Parameters:
        l   (list): The list to be shifted (usually numeric key digits).
        num (int): The number of positions to shift forward.

    Flow:
        1. Takes the input list of key digits.
        2. Rotates elements to the right by 'num' positions.
        3. Returns the new shifted list.

    Example:
        shfit([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]

    Returns:
        list: The circularly shifted list.
    """    
    c = []
    for t in range(len(l)) :
        if num  == 1 :
            c.insert(0 , l[-1])
            for i in range(len(l)) :
                if i == len(l) -1 :
                    pass
                else :
                    c.insert(i+num , l[i])
            break
        if num == 2 :
            c.insert(0 , l[-2])
            c.insert(1 , l[-1])
            for i in range(len(l)) :
                if i == len(l) - 2 or i == len(l) - 1 :
                    pass
                else :
                    c.insert(i+num , l[i])
            break
        if num == 3 :
            c.insert(0 , l[-3])
            c.insert(1 , l[-2])
            c.insert(2 , l[-1])
            for i in range(len(l)) :
                if i == len(l) - 2 or i == len(l) - 1 or i == len(l) - 3  :
                    pass
                else :
                    c.insert(i+num , l[i])
            break            
        if num == 4 :
            c.insert(0 , l[-4])
            c.insert(1 , l[-3])
            c.insert(2 , l[-2])
            c.insert(3 , l[-1])
            for i in range(len(l)) :
                if i == len(l) - 2 or i == len(l) - 1 or i == len(l) - 3  or  i == len(l) - 4  :
                    pass
                else :
                    c.insert(i+num , l[i])
            break            
        if num == 5 :
            c.insert(0 , l[-5])
            c.insert(1 , l[-4])
            c.insert(2 , l[-3])
            c.insert(3 , l[-2])
            c.insert(4 , l[-1])
            for i in range(len(l)) :
                if i == len(l) - 2 or i == len(l) - 1 or i == len(l) - 3  or  i == len(l) - 4 or  i == len(l) - 5  :
                    pass
                else :
                    c.insert(i+num , l[i])
            break           
        if num == 6 :
            c.insert(0 , l[-6])
            c.insert(1 , l[-5])
            c.insert(2 , l[-4])
            c.insert(3 , l[-3])
            c.insert(4 , l[-2])
            c.insert(5 , l[-1])
            for i in range(len(l)) :
                if i == len(l) - 2 or i == len(l) - 1 or i == len(l) - 3  or  i == len(l) - 4 or  i == len(l) - 5 or  i == len(l) - 6 :
                    pass
                else :
                    c.insert(i+num , l[i])
            break           
        if num == 7 :
            c.insert(0 , l[-7])
            c.insert(1 , l[-6])
            c.insert(2 , l[-5])
            c.insert(3 , l[-4])
            c.insert(4 , l[-3])
            c.insert(5 , l[-2])
            c.insert(6 , l[-1])
            for i in range(len(l)) :
                if i == len(l) - 2 or i == len(l) - 1 or i == len(l) - 3  or  i == len(l) - 4 or  i == len(l) - 5 or  i == len(l) - 6 or  i == len(l) - 7 :
                    pass
                else :
                    c.insert(i+num , l[i])
            break           
        if num == 8 :
            c.insert(0 , l[-8])
            c.insert(1 , l[-7])
            c.insert(2 , l[-6])
            c.insert(3 , l[-5])
            c.insert(4 , l[-4])
            c.insert(5 , l[-3])
            c.insert(6 , l[-2])
            c.insert(7 , l[-1])
            for i in range(len(l)) :
                if i == len(l) - 2 or i == len(l) - 1 or i == len(l) - 3  or  i == len(l) - 4 or  i == len(l) - 5 or  i == len(l) - 6 or  i == len(l) - 7 or  i == len(l) - 8 :
                    pass
                else :
                    c.insert(i+num , l[i])
            break           
        if num == 9 :
            c.insert(0 , l[-9])
            c.insert(1 , l[-8])
            c.insert(2 , l[-7])
            c.insert(3 , l[-6])
            c.insert(4 , l[-5])
            c.insert(5 , l[-4])
            c.insert(6 , l[-3])
            c.insert(7 , l[-2])
            c.insert(8 , l[-1])        
            for i in range(len(l)) :
                if i == len(l) - 2 or i == len(l) - 1 or i == len(l) - 3  or  i == len(l) - 4 or  i == len(l) - 5 or  i == len(l) - 6 or  i == len(l) - 7 or  i == len(l) - 8 or  i == len(l) - 9 :
                    pass
                else :
                    c.insert(i+num , l[i])
            break
        if num == 10 :
            c.insert(0 , l[-10])            
            c.insert(1 , l[-9])
            c.insert(2 , l[-8])
            c.insert(3 , l[-7])
            c.insert(4 , l[-6])
            c.insert(5 , l[-5])
            c.insert(6 , l[-4])
            c.insert(7 , l[-3])
            c.insert(8 , l[-2])
            c.insert(9 , l[-1])        
            for i in range(len(l)) :
                if i == len(l) - 2 or i == len(l) - 1 or i == len(l) - 3  or  i == len(l) - 4 or  i == len(l) - 5 or  i == len(l) - 6 or  i == len(l) - 7 or  i == len(l) - 8 or  i == len(l) - 9 or  i == len(l) - 10 :
                    pass
                else :
                    c.insert(i+num , l[i])
            break  
        if num == 11 :
            c.insert(0 , l[-11])            
            c.insert(1 , l[-10])
            c.insert(2 , l[-9])
            c.insert(3 , l[-8])
            c.insert(4 , l[-7])
            c.insert(5 , l[-6])
            c.insert(6 , l[-5])
            c.insert(7 , l[-4])
            c.insert(8 , l[-3])
            c.insert(9 , l[-2])
            c.insert(10 , l[-1])              
            for i in range(len(l)) :
                if i == len(l) - 2 or i == len(l) - 1 or i == len(l) - 3  or  i == len(l) - 4 or  i == len(l) - 5 or  i == len(l) - 6 or  i == len(l) - 7 or  i == len(l) - 8 or  i == len(l) - 9 or  i == len(l) - 10 or  i == len(l) - 11  :
                    pass
                else :
                    c.insert(i+num , l[i])
            break  
        if num == 12 :
            c.insert(0 , l[-12])  
            c.insert(1 , l[-11])            
            c.insert(2 , l[-10])
            c.insert(3 , l[-9])
            c.insert(4 , l[-8])
            c.insert(5 , l[-7])
            c.insert(6 , l[-6])
            c.insert(7 , l[-5])
            c.insert(8 , l[-4])
            c.insert(9 , l[-3])
            c.insert(10 , l[-2])
            c.insert(11 , l[-1]) 

            for i in range(len(l)) :
                if i == len(l) - 2 or i == len(l) - 1 or i == len(l) - 3  or  i == len(l) - 4 or  i == len(l) - 5 or  i == len(l) - 6 or  i == len(l) - 7 or  i == len(l) - 8 or  i == len(l) - 9 or  i == len(l) - 10 or  i == len(l) - 11 or  i == len(l) - 12:
                    pass
                else :
                    c.insert(i+num , l[i])
            break  
        if num == 13 :
            c.insert(0 , l[-13])             
            c.insert(1 , l[-12])  
            c.insert(2 , l[-11])            
            c.insert(3 , l[-10])
            c.insert(4 , l[-9])
            c.insert(5 , l[-8])
            c.insert(6 , l[-7])
            c.insert(7 , l[-6])
            c.insert(8 , l[-5])
            c.insert(9 , l[-4])
            c.insert(10 , l[-3])
            c.insert(11 , l[-2])
            c.insert(12 , l[-1])         
            for i in range(len(l)) :
                if i == len(l) - 2 or i == len(l) - 1 or i == len(l) - 3  or  i == len(l) - 4 or  i == len(l) - 5 or  i == len(l) - 6 or  i == len(l) - 7 or  i == len(l) - 8 or  i == len(l) - 9 or  i == len(l) - 10 or  i == len(l) - 11 or  i == len(l) - 12 or  i == len(l) - 13 :
                    pass
                else :
                    c.insert(i+num , l[i])
            break  
        if num == 14 :
            c.insert(0 , l[-14])             
            c.insert(1 , l[-13])             
            c.insert(2 , l[-12])  
            c.insert(3 , l[-11])            
            c.insert(4 , l[-10])
            c.insert(5 , l[-9])
            c.insert(6 , l[-8])
            c.insert(7 , l[-7])
            c.insert(8 , l[-6])
            c.insert(9 , l[-5])
            c.insert(10 , l[-4])
            c.insert(11 , l[-3])
            c.insert(12 , l[-2])
            c.insert(13 , l[-1])        
            for i in range(len(l)) :
                if i == len(l) - 2 or i == len(l) - 1 or i == len(l) - 3  or  i == len(l) - 4 or  i == len(l) - 5 or  i == len(l) - 6 or  i == len(l) - 7 or  i == len(l) - 8 or  i == len(l) - 9 or  i == len(l) - 10 or  i == len(l) - 11 or  i == len(l) - 12 or  i == len(l) - 13 or  i == len(l) - 14  :
                    pass
                else :
                    c.insert(i+num , l[i])
            break  
        if num == 15 :
            c.insert(0 , l[-15]) 
            c.insert(1 , l[-14])             
            c.insert(2 , l[-13])             
            c.insert(3 , l[-12])  
            c.insert(4 , l[-11])            
            c.insert(5 , l[-10])
            c.insert(6 , l[-9])
            c.insert(7 , l[-8])
            c.insert(8 , l[-7])
            c.insert(9 , l[-6])
            c.insert(10 , l[-5])
            c.insert(11 , l[-4])
            c.insert(12 , l[-3])
            c.insert(13 , l[-2])
            c.insert(14 , l[-1])           
            for i in range(len(l)) :
                if i == len(l) - 2 or i == len(l) - 1 or i == len(l) - 3  or  i == len(l) - 4 or  i == len(l) - 5 or  i == len(l) - 6 or  i == len(l) - 7 or  i == len(l) - 8 or  i == len(l) - 9 or  i == len(l) - 10 or  i == len(l) - 11 or  i == len(l) - 12 or  i == len(l) - 13 or  i == len(l) - 14 or  i == len(l) - 15 :
                    pass
                else :
                    c.insert(i+num , l[i])
            break         
    return c


def unshfit(l :list ,  num : int):
    """
    Function: unshfit
    -----------------
    Reverses the circular shift applied by the 'shfit' function.
    Used in the ASENFA decryption process to restore the original order
    of digits before reconstructing the real key.

    Parameters:
        l   (list): The shifted list to be restored.
        num (int): The number of positions that were originally shifted.

    Flow:
        1. Takes the shifted key digits.
        2. Rotates elements to the left by 'num' positions.
        3. Returns the original (unshifted) list.

    Example:
        unshfit([4, 5, 1, 2, 3], 2) -> [1, 2, 3, 4, 5]

    Returns:
        list: The list restored to its original order.
    """

    c = []
    for t in range(len(l)) :
        if num  == 1 :
            for i in range(len(l)) :
                if i == len(l) -1 :
                    c.append(l[0])
                else:
                    c.insert(i+num , l[i+num])
        break 
    if num  == 2 :
            for i in range(len(l)) :
                if i == len(l) - 1  or i == len(l) - 2 :
                    c.append(l[0])
                    c.append(l[1])
                    break
                else:
                    c.insert(i+num , l[i+num])
    if num  == 3 :
            for i in range(len(l)) :
                if i == len(l) - 1  or i == len(l) - 2 or i == len(l) - 3:
                    c.append(l[0])
                    c.append(l[1])
                    c.append(l[2])
                    break
                else:
                    c.insert(i+num , l[i+num])
    if num  == 4 :
            for i in range(len(l)) :
                if i == len(l) - 1  or i == len(l) - 2 or i == len(l) - 3 or i == len(l) - 4:
                    c.append(l[0])
                    c.append(l[1])
                    c.append(l[2])
                    c.append(l[3])
                    break
                else:
                    c.insert(i+num , l[i+num])     
    if num  == 5 :
            for i in range(len(l)) :
                if i == len(l) - 1  or i == len(l) - 2 or i == len(l) - 3 or i == len(l) - 4 or i == len(l) - 5:
                    c.append(l[0])
                    c.append(l[1])
                    c.append(l[2])
                    c.append(l[3])
                    c.append(l[4])                    
                    break
                else:
                    c.insert(i+num , l[i+num])        
    if num  == 6 :
            for i in range(len(l)) :
                if i == len(l) - 1  or i == len(l) - 2 or i == len(l) - 3 or i == len(l) - 4 or i == len(l) - 5 or i == len(l) - 6:
                    c.append(l[0])
                    c.append(l[1])
                    c.append(l[2])
                    c.append(l[3])
                    c.append(l[4])         
                    c.append(l[5])                                  
                    break
                else:
                    c.insert(i+num , l[i+num])    
    if num  == 7 :
            for i in range(len(l)) :
                if i == len(l) - 1  or i == len(l) - 2 or i == len(l) - 3 or i == len(l) - 4 or i == len(l) - 5 or i == len(l) - 6 or i == len(l) - 7:
                    c.append(l[0])
                    c.append(l[1])
                    c.append(l[2])
                    c.append(l[3])
                    c.append(l[4])         
                    c.append(l[5]) 
                    c.append(l[6])                                    
                    break
                else:
                    c.insert(i+num , l[i+num])  
    if num  == 8 :
            for i in range(len(l)) :
                if i == len(l) - 1  or i == len(l) - 2 or i == len(l) - 3 or i == len(l) - 4 or i == len(l) - 5 or i == len(l) - 6 or i == len(l) - 7 or i == len(l) - 8:
                    c.append(l[0])
                    c.append(l[1])
                    c.append(l[2])
                    c.append(l[3])
                    c.append(l[4])         
                    c.append(l[5]) 
                    c.append(l[6])
                    c.append(l[7])                                                           
                    break
                else:
                    c.insert(i+num , l[i+num])  
    if num  == 9 :
            for i in range(len(l)) :
                if i == len(l) - 1  or i == len(l) - 2 or i == len(l) - 3 or i == len(l) - 4 or i == len(l) - 5 or i == len(l) - 6 or i == len(l) - 7 or i == len(l) - 8 or i == len(l) - 9:
                    c.append(l[0])
                    c.append(l[1])
                    c.append(l[2])
                    c.append(l[3])
                    c.append(l[4])         
                    c.append(l[5]) 
                    c.append(l[6])
                    c.append(l[7])
                    c.append(l[8])                                                                               
                    break
                else:
                    c.insert(i+num , l[i+num])
    if num  == 10 :
            for i in range(len(l)) :
                if i == len(l) - 1  or i == len(l) - 2 or i == len(l) - 3 or i == len(l) - 4 or i == len(l) - 5 or i == len(l) - 6 or i == len(l) - 7 or i == len(l) - 8 or i == len(l) - 9 or i == len(l) - 10:
                    c.append(l[0])
                    c.append(l[1])
                    c.append(l[2])
                    c.append(l[3])
                    c.append(l[4])         
                    c.append(l[5]) 
                    c.append(l[6])
                    c.append(l[7])
                    c.append(l[8])  
                    c.append(l[9])                                                                             
                    break
                else:
                    c.insert(i+num , l[i+num])             
    if num  == 11 :
            for i in range(len(l)) :
                if i == len(l) - 1  or i == len(l) - 2 or i == len(l) - 3 or i == len(l) - 4 or i == len(l) - 5 or i == len(l) - 6 or i == len(l) - 7 or i == len(l) - 8 or i == len(l) - 9 or i == len(l) - 11 :
                    c.append(l[0])
                    c.append(l[1])
                    c.append(l[2])
                    c.append(l[3])
                    c.append(l[4])         
                    c.append(l[5]) 
                    c.append(l[6])
                    c.append(l[7])
                    c.append(l[8])  
                    c.append(l[9]) 
                    c.append(l[10])                                                                                                 
                    break
                else:
                    c.insert(i+num , l[i+num])
    if num  == 12 :
            for i in range(len(l)) :
                if i == len(l) - 1  or i == len(l) - 2 or i == len(l) - 3 or i == len(l) - 4 or i == len(l) - 5 or i == len(l) - 6 or i == len(l) - 7 or i == len(l) - 8 or i == len(l) - 9 or i == len(l) - 11 or i == len(l) - 12 :
                    c.append(l[0])
                    c.append(l[1])
                    c.append(l[2])
                    c.append(l[3])
                    c.append(l[4])         
                    c.append(l[5]) 
                    c.append(l[6])
                    c.append(l[7])
                    c.append(l[8])  
                    c.append(l[9]) 
                    c.append(l[10]) 
                    c.append(l[11])                                                                                                    
                    break
                else:
                    c.insert(i+num , l[i+num])  
    if num  == 13 :
            for i in range(len(l)) :
                if i == len(l) - 1  or i == len(l) - 2 or i == len(l) - 3 or i == len(l) - 4 or i == len(l) - 5 or i == len(l) - 6 or i == len(l) - 7 or i == len(l) - 8 or i == len(l) - 9 or i == len(l) - 11 or i == len(l) - 12 or i == len(l) - 13 :
                    c.append(l[0])
                    c.append(l[1])
                    c.append(l[2])
                    c.append(l[3])
                    c.append(l[4])         
                    c.append(l[5]) 
                    c.append(l[6])
                    c.append(l[7])
                    c.append(l[8])  
                    c.append(l[9]) 
                    c.append(l[10]) 
                    c.append(l[11]) 
                    c.append(l[12])                                                                                                   
                    break
                else:
                    c.insert(i+num , l[i+num])
    if num  == 14 :
            for i in range(len(l)) :
                if i == len(l) - 1  or i == len(l) - 2 or i == len(l) - 3 or i == len(l) - 4 or i == len(l) - 5 or i == len(l) - 6 or i == len(l) - 7 or i == len(l) - 8 or i == len(l) - 9 or i == len(l) - 11 or i == len(l) - 12 or i == len(l) - 13 or i == len(l) - 14 :
                    c.append(l[0])
                    c.append(l[1])
                    c.append(l[2])
                    c.append(l[3])
                    c.append(l[4])         
                    c.append(l[5]) 
                    c.append(l[6])
                    c.append(l[7])
                    c.append(l[8])  
                    c.append(l[9]) 
                    c.append(l[10]) 
                    c.append(l[11]) 
                    c.append(l[12])  
                    c.append(l[13])                                                                                                 
                    break
                else:
                    c.insert(i+num , l[i+num])        
    if num  == 15 :
            for i in range(len(l)) :
                if i == len(l) - 1  or i == len(l) - 2 or i == len(l) - 3 or i == len(l) - 4 or i == len(l) - 5 or i == len(l) - 6 or i == len(l) - 7 or i == len(l) - 8 or i == len(l) - 9 or i == len(l) - 11 or i == len(l) - 12 or i == len(l) - 13 or i == len(l) - 14 or i == len(l) - 15 :
                    c.append(l[0])
                    c.append(l[1])
                    c.append(l[2])
                    c.append(l[3])
                    c.append(l[4])         
                    c.append(l[5]) 
                    c.append(l[6])
                    c.append(l[7])
                    c.append(l[8])  
                    c.append(l[9]) 
                    c.append(l[10]) 
                    c.append(l[11]) 
                    c.append(l[12])  
                    c.append(l[13])
                    c.append(l[14])                                                                                                                      
                    break
                else:
                    c.insert(i+num , l[i+num])                                                                                                                                                                                                                                  
    return c

