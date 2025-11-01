#include<iostream>
using namespace std;

int main() {

    int numbers[]{32,435,653,65,234,6367,876,327,564};
    int max = numbers[0];
    for(int i = 0;i < 9;i++){
        if(numbers[i] > max){
            max = numbers[i];
        }
    }
cout << max;

return 0;
}