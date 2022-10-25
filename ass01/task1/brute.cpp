#include <iostream>
using namespace std;

int main()
{
    int arr[] = {0,1,1,0,0,1,0,0,1};
    int len = sizeof(arr)/sizeof(arr[0]);
    
    for(int i=1; i< len; i=i+2){
        
        if (arr[i] == 1)
            arr[i] = 0;
        else
            arr[i] = 1;
    }
    for(int i = 0; i<len;i++){
        cout<<arr[i]<<endl;
    }
    
    return 0;
}
