
Code: #include <iostream>
using namespace std;
 
// DFA
void q1(string, int);
void q2(string, int);
void q3(string, int);
void q4(string, int);
 
//  Q1
void q1(string s, int i)
{
 
    if (i == s.length()) {
        cout << "Yes \n";
        return;
    }
 
  
    if (s[i] == 'a')
        q1(s, i + 1);
    else
        q2(s, i + 1);
}
 
//  Q2
void q2(string s, int i)
{
    if (i == s.length()) {
        cout << "No \n";
        return;
    }
 
        if (s[i] == 'a')
        q1(s, i + 1);
    else
        q2(s, i + 1);
}
 
// Q3
void q3(string s, int i)
{
    if (i == s.length()) {
        cout << "Yes \n";
        return;
    }

    if (s[i] == 'a')
        q4(s, i + 1);
    else
        q3(s, i + 1);
}
 
//  Q4
void q4(string s, int i)
{
    if (i == s.length()) {
        cout << "No \n";
        return;
    }
 
    if (s[i] == 'a')
        q4(s, i + 1);
    else
        q3(s, i + 1);
}
 
//  Q0
void q0(string s, int i)
{
 
    if (i == s.length()) {
        cout << "No \n";
        return;
    }

    if (s[i] == 'a')
        q1(s, i + 1);
    else
        q3(s, i + 1);
}

int main()
{
    string s = "abbaabb";

    q0(s, 0);
}
