#include <iostream>


int GuessNumber(int target){

    int number = 0;
    std::cin>>number;

    while (true){

    if (number < target){
        std::cout << "it's higher";
    }
    else if (number > target) {
        std::cout << "it's lower";
    }

    std::cout << "good job you have it";


    }
}

std::map<std::string,int> WordsLowerCase(std::string paragraphe){

    for (char& letter : paragraphe){
        if (std::ispunct(static_cast<char>(letter))){
            c = ' ';
        }
        else {
            std::tolower(letter);
        }
    }

    std::stringstream ss(paragraphe);
    std::string mot;
    std::vector<std::string> mots;

    while (ss >> mot){
        mots.push_back(mot);
    }

    std::map<std::string,int> dict;



    for (std::string& word : paragraphe){
        if (dict.contains(word)){
            dict[word]+=1;
        }
        else{
            dict[word] = 1;
        }

    }
    return dict;
};


int main(){

    GuessNumber(300);
    return 0;
}


