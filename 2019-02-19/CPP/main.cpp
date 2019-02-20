#include <iostream>
#include <string>

using namespace std;


int getInput();


int main()
{
  int num;
  num = getInput();
  while (num > 0)
  {
    string str = to_string(num);
    int persistence = 0;
    while (str.size() > 1){
      int x = 0;
      for(int i = 0; i < str.size(); i++){
        x += (int)str[i] - 48;
      }
      str = to_string(x);
      persistence++;
    }

    cout << "final number: " << str << "\n";
    cout << "Additive persistence: " << persistence << "\n";

    num = getInput();
  }
}


int getInput()
{
  int input;
  cout << "Enter a negative number to exit. \n";
  cout << "Input a number to find it's additive persistence: ";
  cin >> input;
  return input;
}
