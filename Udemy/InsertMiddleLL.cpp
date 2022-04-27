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

void insertAtMiddle(node* & head,int data, int pos)
{
    if(pos == 0){
        //call insert at the head
        insertAtHead(head,data);
    }
    else
    {
      
        //find the right place for insertion first
        //for that iterate till the position
        node* temp = head;//storing the address of head node
        for(int i = 0; i<pos-1 ; i++)
        {
            temp = head->next;
        }
        //now create the new node to insert it
        node* newnode = new node(data);
        //now set the newnode next pointer to temp-next & previous temp->next to the new node inserted
        newnode->next = temp->next;
        temp->next = newnode;

    }

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
    insertAtMiddle(head,10,3);
    printList(head);
    return 0;
}

