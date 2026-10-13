#include <iostream>

struct Node{
    int value;
    Node* left;
    Node* right;

    Node(int val) : value(val), left(nullptr), right(nullptr) {}

};

bool contient_valeur_recursif(const Node* root, int cible){

    if (root == nullptr){
        return false;
    }
    if (root->value == cible){
        return true;
    }

    if (root->value > cible){
        return contient_valeur_recursif(root->left, cible);
    }
    if (root->value < cible){
        return contient_valeur_recursif(root->right, cible);
    }

return false;
}


