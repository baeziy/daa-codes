#include <iostream>
using namespace std;

int main()
{
    int arr[] = {8, 8, 8, 9, 9, 10 , 10, 10, 10};
    int len = sizeof(arr)/sizeof(arr[0]);
    int count = 0;
    for(int i=0;i < len; i++){
        if(arr[i] == 9){
            count++;
        }
    }
    cout<<count;
    return 0;
}
