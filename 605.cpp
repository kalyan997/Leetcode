class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if(n==0){
            return true;
        }
        if(flowerbed[0]==0 and n>0){
            if(flowerbed.size()>1 and flowerbed[1]==0){
                flowerbed[0] = 1;
                n--;
            }
            if(flowerbed.size()==1){
                flowerbed[0] = 1;
                n--;
            }
        }
        for(int i=1;i<flowerbed.size()-1;i++){
            if(n==0){
                return true;
            }
            if(flowerbed[i]==0 and n>0){
                if(flowerbed[i-1]==0 and flowerbed[i+1]==0){
                    flowerbed[i] = 1;
                    n--;
                }
            }
        }
        if(flowerbed[flowerbed.size()-1]==0 and n>0){
            if(flowerbed.size()>1 and flowerbed[flowerbed.size()-2]==0){
                flowerbed[flowerbed.size()-1] = 1;
                n--;
            }
        }
        return n==0?true:false;
    }
};