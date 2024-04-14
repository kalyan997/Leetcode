class Solution {
public:
    int fib(int n) {
        
        double r1 = (sqrt(5) + 1) / 2;
        //double r2 = (sqrt(5) - 1) / 2;
        return round(pow(r1, n) / sqrt(5));
        
    }
};