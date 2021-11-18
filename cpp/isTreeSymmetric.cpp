#include <iostream>

using namespace std;

template<typename T>
struct Tree {
  Tree(const T &v) : value(v), left(nullptr), right(nullptr) {}
  T value;
  Tree *left;
  Tree *right;
};


bool isTreeSymmetric(Tree<int> * t) {
    if (!t || !t -> left && !t -> right)
        return true;
        
    else if (t -> left && t -> right) {
        Tree<int> *temp1 = new Tree<int> (t -> value);
        Tree<int> *temp2 = new Tree<int> (t -> value);

	        
        temp1 -> left = t -> left -> left;
        temp1 -> right = t -> right -> right;
        
        temp2 -> left = t -> left -> right;
        temp2 -> right = t -> right -> left;
	
	cout << "temp1 = " << temp1 -> value << "-> left " << temp1 -> left -> value << "-> right " << temp1 -> right -> value << "\ntemp2 = " << temp2 -> value << "-> left " << temp2 -> left -> value << "-> right " << temp2 -> right -> value << endl;

        if (t -> left -> value == t -> right -> value)
            return isTreeSymmetric(temp1) &&  isTreeSymmetric(temp2);
    }
    return false;
}

int main()
{
  // Creating a tree.
  Tree<int> *root = new Tree<int>(1); 
  root -> left = new Tree<int>(2); 
  root -> right = new Tree<int>(2); 
  root -> left -> left = new Tree<int>(3); 
  root -> left -> right = new Tree<int>(4);
  root -> right -> left = new Tree<int>(4);
  root -> right -> right = new Tree<int>(3);
  if (isTreeSymmetric(root)){
    cout<<"The binary tree is symmetric."<<endl;
  }
  else{
    cout<<"The binary tree is asymmetric."<<endl;
  }
  return 0;
}
