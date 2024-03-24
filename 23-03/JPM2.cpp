#include<bits/stdc++.h>


using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

int binaryToDecimal(ListNode *head)
{
    int decimal = 0;
    int power = 0;

    while (head != nullptr)
    {
        decimal += head->val * pow(2, power);
        head = head->next;
        power++;
    }

    return decimal;
}

void printLinkedList(ListNode *head)
{
    while (head != nullptr)
    {
        cout << head->val << " -> ";
        head = head->next;
    }
    cout << "NULL" << endl;
}

int main()
{
    ListNode *head = new ListNode(1);
    head->next = new ListNode(0);
    head->next->next = new ListNode(1);
    head->next->next->next = new ListNode(1);
    head->next->next->next->next = new ListNode(0);

    cout << "Linked List: ";
    printLinkedList(head);

    int decimal = binaryToDecimal(head);
    cout << "Decimal representation: " << decimal << endl;

    while (head != nullptr)
    {
        ListNode *temp = head;
        head = head->next;
        delete temp;
    }

    return 0;
}
