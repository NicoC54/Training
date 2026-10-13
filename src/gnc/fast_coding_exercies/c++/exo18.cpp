#include <iostream>
#include <string>
#include <stack> // La structure idéale pour ce problème

bool est_trame_valide(const std::string& trame) {

    if (trame == ""){
        return true;
    }

    std::stack<char> stack;

    for (char parenthese : trame){

        if ((parenthese == '[') || (parenthese == '(') || (parenthese == '{')){
            stack.push(parenthese);
        }

        else if (parenthese == ']'){
            if (stack.empty()){
                return false;
            }
             
            char ouverture = stack.top();
            stack.pop();
            if (ouverture != '['){
                return false;
            }
        }

         else if (parenthese == ')'){
            if (stack.empty()){
                return false;
            }
             
            char ouverture = stack.top();
            stack.pop();
            if (ouverture != '('){
                return false;
            }
        }

        else if (parenthese == '}'){
            if (stack.empty()){
                return false;
            }
             
            char ouverture = stack.top();
            stack.pop();
            if (ouverture != '{'){
                return false;
            }
        }
        }


    if (stack.empty()) {
        return true;
    }

    return false; 

}

// --- BLOC DE TESTS ---
int main() {
    std::cout << std::boolalpha; // Permet d'afficher "true" ou "false" au lieu de "1" ou "0"

    // Test 1 : Trames simples valides
    std::cout << "Test 1 : " << est_trame_valide("()") << " (Attendu : true)" << std::endl;
    std::cout << "Test 2 : " << est_trame_valide("()[]{}") << " (Attendu : true)" << std::endl;

    // Test 3 : Trame imbriquée valide
    std::cout << "Test 3 : " << est_trame_valide("{[]}") << " (Attendu : true)" << std::endl;

    // Test 4 : Trames invalides (mauvais caractère ou mauvais ordre)
    std::cout << "Test 4 : " << est_trame_valide("(]") << " (Attendu : false)" << std::endl;
    std::cout << "Test 5 : " << est_trame_valide("([)]") << " (Attendu : false)" << std::endl;

    // Test 6 : Trame incomplète
    std::cout << "Test 6 : " << est_trame_valide("[") << " (Attendu : false)" << std::endl;
    std::cout << "Test 7 : " << est_trame_valide("]") << " (Attendu : false)" << std::endl;

    return 0;
}