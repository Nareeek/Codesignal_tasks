//
// Binary trees are already defined with this interface:
// template<typename T>
// struct Tree {
//   Tree(const T &v) : value(v), left(nullptr), right(nullptr) {}
//   T value;
//   Tree *left;
//   Tree *right;
// };
bool solution(Tree<int> *t, int s) {
  if (t == nullptr)
    return false;
    
  if (!t->left && !t->right && s == t->value)
      return true;
      
  else if (t->left && t->right)
    return (solution(t->left, s - (t->value)) || solution(t->right, s - (t->value)));
    
  else if (t->right)
    return (solution(t->right, s - (t->value)));
        
  else if (t->left)
    return (solution(t->left, s - (t->value)));
        
  return false;
}