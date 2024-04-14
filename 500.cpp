class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        unordered_map<char,int> alph_row;
        vector<string> rows;
        vector<string> res;
        rows.push_back("qwertyuiop");
        rows.push_back("asdfghjkl");
        rows.push_back("zxcvbnm");
        for(int i=0;i<rows.size();i++){
            for(char alph: rows[i]){
                alph_row[alph] = i+1;
            }
        }
        for(string word: words){
            int row = alph_row[tolower(word[0])];
            int same_row = 1;
            for(char alph: word){
                alph = tolower(alph);
                if(alph_row[alph]!=row){
                    same_row = 0;
                    break;
                }
            }
            if(same_row==1){
                res.push_back(word);
            }
        }
        return res;
    }
};