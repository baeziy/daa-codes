#include <iostream>
using namespace std;

int main()
{
    int arr[] = {3,4,5,7};
    int len = sizeof(arr)/sizeof(arr[0]);
    int sum = 0;
    for(int i=0;i < len; i++){
        if((arr[i] > len - 100) && (arr[i] < len + 100)){
            sum += arr[i];
        }
    }
    cout<<sum;
    return 0;
}
