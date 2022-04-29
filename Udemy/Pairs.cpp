// Qn: given an array containing N intgers, and an number Sum denoting a target sum.
// find two distinct intgers that can pair up to form target sum.
//input : array = [10,5,2,3,-6,9,11]
//Sum = 4
//Output = [10, -6]
//Try this code using c++
#include<iostream>
#include<vector>
#include<unordered_set>

using namespace std;

vector<int> pairSum(vector<int> arr, int Sum);


int main(){
    vector<int> arr{10,5,2,3,-6,9,11};
    int Sum = 4;
    auto p = pairSum(arr,Sum);
    if(p.size()==0)
        cout<<"No such pair exist"<<endl;
    else
        cout<<p[0]<<","<<p[1];

    return 0;
}

vector<int> pairSum(vector<int> arr, int Sum)
{
    vector<int> result;
    unordered_set<int> s;

    for(int i = 0; i < arr.size();i++)
    {
        int x = Sum - arr[i];
        if(s.find(x)!=s.end())
        {
            result.push_back(x);
            result.push_back(arr[i]);
            return result;
        }
        s.insert(arr[i]);
    }
    return {};

}
