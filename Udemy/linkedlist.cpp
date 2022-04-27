#include <iostream>
using namespace std;

class node
{
    public:
        int data;
        node* next;

        node(int data)
        {
            this->data = data;
            next = NULL; 
        }
};

void insertAtHead(node * &head, int data)
{
    if(head == NULL)
    {
        head = new node(data);
        return;
    }

    node* n = new node(data);
    n->next = head;
    head = n;
}

void printList(node * head)
{
    while(head != NULL)
    {
        cout<<head->data<<"->";
        //cout<<"\t";
        head = head->next;
    }
cout<<endl;
}
int main()
{
    node * head = NULL;
    insertAtHead(head,4);
     insertAtHead(head,3);
      insertAtHead(head,2);
       insertAtHead(head,1);
        insertAtHead(head,0);
    printList(head);
    return 0;
}

