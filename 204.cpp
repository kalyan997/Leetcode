class Solution {
public:
    int countPrimes(int n) {
        int count = 0;
        if(n<2){
            return 0;
        }
        
        vector<bool> numbers(n);
        for(int p=2;p<=sqrt(n);p++){
            if(numbers[p]==false){
                for(int j =p*p;j<n;j+=p){
                    numbers[j] = true;
                }
            }
        }
        
        for(int i=2;i<n;i++){
            if(numbers[i]==false){
                count++;
            }
        }
        return count;
    }
};