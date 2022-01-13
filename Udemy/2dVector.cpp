//2D Vector , like 2D Array

#include<iostream>
#include<vector>
using namespace std;
int main(){

	vector <vector<int>> arr{
		{1,2,3},// This is row 1
		{4,5,6},//this is row 2
		{7,8,9,10},//this is row 3 with 4 elements
		{11,12}//this is row 4 with 2 elements
	};

	// to print values , use below code

	for(int i = 0; i < arr.size();i++)
	{
		//arr[0] is first row

		for(int number:arr[i])
			cout<<number<<",";
		cout<<endl;
	}
}