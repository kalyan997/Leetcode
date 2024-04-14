class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_map<string,int> email_count;
        for(string email: emails){
            string curr_email = "";
            for(int i=0;i<email.size();i++){
                //cout<<i<<curr_email<<"\n";
                if(email[i]=='@'){
                    //cout<<email.substr(i,email.size()-i)<<"\n";
                    curr_email += email.substr(i,email.size()-i);
                    break;
                }
                else if(email[i]=='+'){
                    while(email[i]!='@'){
                        i++;
                    }
                    i--;
                    continue;
                }
                else if(email[i]=='.'){
                   continue;
                }
                curr_email += email[i];
            }
            email_count[curr_email]++;
        }
        
        /*for(auto email_ : email_count){
            cout<<email_.first<<"\n";
        }*/
        return email_count.size();
    }
};