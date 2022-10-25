#include <iostream>
using namespace std;

int main()
{
    int arr[] = {3,4,5,7};
    int len = sizeof(arr)/sizeof(arr[0]);
    int product = 1;
    for(int i=0;i < len; i++){
        product = product * arr[i];
    }
    cout<<product;
    return 0;
}
