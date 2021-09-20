#include <algorithm>
#include <iostream>
#include <vector>

using std::vector;

int get_majority_element_simple(vector<int> &a, int left, int right) {
  if (left == right) return -1;
  if (left + 1 == right) return a[left];
  int currentElement;
  int count;
  for (int i = 0 ; i < right ;i++){
      currentElement = a[i];
      count = 0;
      for (int j = 0 ; j < right ;j++){
          if(a[j] == currentElement){
              count++;
          }
      }
      if (count > right/2){
              return a[i];
      }
  }
  return 0;
}

int get_majority_element_hard(vector<int> &a, int left, int right) {
    if (left == right) return -1;
    if (left + 1 == right) return a[left];
    int maj_index = 0, count = 1;
    for (int i = left+1; i < right; i++) {
        if (a[maj_index] == a[i])
            count++;
        else
            count--;
        if (count == 0) {
            maj_index = i;
            count = 1;
        }
    }
    int count2 = 0;
    for (int i = 0; i < right; i++){
        if (a[i] == a[maj_index])
                count2++;
    }
    if (count2 > a.size() / 2)
        return 1;
    else
        return 0;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  std::cout << get_majority_element_hard(a, 0, a.size())<< '\n';

}
