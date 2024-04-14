class Solution {
public:
    bool detectCapitalUse(string word) {
        return All_Lowers(word)||All_Capitals(word)||First_capital(word);
    }
    
    bool All_Lowers(string word){
        for(char c:word){
            if(c<'a'){
                return false;
            }
        }
        return true;
    }
    bool All_Capitals(string word){
        for(char c:word){
            if(c>'Z'){
                return false;
            }
        }
        return true;
    }
    
    bool First_capital(string word){
        if(word[0]>'Z'){
            return false;
        }
        for(int i=1;i<word.size();i++){
            if(word[i]<='Z'){
                return false;
            }
        }
        return true;
    }
};