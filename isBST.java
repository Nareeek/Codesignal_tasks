//
// Binary trees are already defined with this interface:
// class Tree<T> {
//   Tree(T x) {
//     value = x;
//   }
//   T value;
//   Tree<T> left;
//   Tree<T> right;
// }
List<Integer> l = new ArrayList();

void makeList(Tree<Integer> t) {
  if (t != null) {
    makeList(t.left);
    l.add(t.value);
    makeList(t.right);
  }
}

boolean isBST(Tree<Integer> t) {
  makeList(t);
  
  for (int i = 1; i < l.size(); i++) {
    if (l.get(i - 1) >= l.get(i)) {
      return false;
    }
  }
  
  return true;
}
