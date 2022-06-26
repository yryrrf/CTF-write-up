#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> n = {16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14};
/*
We see that there are many numbers in the picture, a '{' is followed by 7 sets of number, 16 9 3 15 3 20 6
So making an assumption it represents picoctf, 16 is the number representing 'p', it may be an ASCII code encryption
a b c d e f g h i j  k  l  m  n  o  p ...
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ...
we can match it one by one or just write a little program to do it.
*/
int main()
{
    for(int i = 0; i<n.size(); i++) {
        cout<<(char) ('p'-16+n[i]);
    }
}