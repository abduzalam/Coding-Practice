#include <iostream>
#include <vector>
using namespace std;
int main()
{
	//cout<<"Hello World!!";

	vector<int> arr = {1,2,10,12,15};
	arr.push_back(16);
	//size() of the vector No.of elements
	//capacity of the vector means how much total size the vector currently 
	//capacity is not related to no.of elements in the vector
	//
	for(int i=0;i<arr.size();i++)
		cout<<arr[i] <<endl;
	cout<<arr.capacity()<<endl;//Result 10
	//Capacity is 10 because vector is initialized with 5 elements
	//Capacity is double of initialized size
	//If arr size reaches 10, then vector automatically expand to capacity 20
	arr.push_back(17);
	arr.push_back(18);
	arr.push_back(19);
	arr.push_back(20);
	arr.push_back(21);
	cout<<arr.capacity()<<endl;//Capacity is now 20

	//pop_back : remove element from back
	//insert , erase functions

	//Fill Constructore

	vector<int> arr1 (10,7);// This will create vector with 10 elements and each element value = 7
	for(int i=0;i<arr1.size();i++)
		cout<<arr1[i] <<endl;

	arr1.push_back(100);
	//for each format
	arr1.pop_back();//remove 100 from arr1 array..
	for( int number:arr1)
		cout<<number<<endl;
	return 0;
}
