#include <iostream>
using namespace std;

int main()
{
    int arr[] = {2,7,3,14,21};
    int len = sizeof(arr)/sizeof(arr[0]);
    int mul = 1;
    for(int i=0; i<len;i++){
        if (arr[i] % 7 == 0){
            mul = mul* arr[i];
        }
    }
    cout<<mul;
    
    return 0;
}
