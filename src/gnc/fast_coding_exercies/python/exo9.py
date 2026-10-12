def est_trame_valide(trame):

    stack = []

    if trame == "":
        return True

    for i in range (len(trame)):
        if trame[i]=='[' or trame[i]=='{' or trame[i] == '(':
            stack.append(trame[i])

        if trame[i]==']':
            if not stack:
                return False
            parenthese_ouvrante = stack.pop()
            if parenthese_ouvrante != '[':
                return False
        
        if trame[i]==')':
            if not stack:
                return False
            parenthese_ouvrante = stack.pop()
            if parenthese_ouvrante != '(':
                return False


        if trame[i]=='}':
            if not stack:
                return False
            parenthese_ouvrante = stack.pop()
            if parenthese_ouvrante != '{':
                return False
    
    if not stack:
        return True
    
    return False


        
        


    


    
    





# --- BLOC DE TESTS ---
if __name__ == "__main__":
    # Test 1 : Valide et basique
    print(f"Test 1 : {est_trame_valide('{[()]}')}") 
    # Attendu : True

    # Test 2 : Invalide (Mauvais ordre de fermeture)
    print(f"Test 2 : {est_trame_valide('{[(])}')}") 
    # Attendu : False

    # Test 3 : Invalide (Il manque une fermeture)
    print(f"Test 3 : {est_trame_valide('[()')}") 
    # Attendu : False

    # Test 4 : Le Edge Case fatal (Fermeture sans ouverture)
    print(f"Test 4 : {est_trame_valide(']')}") 
    # Attendu : False