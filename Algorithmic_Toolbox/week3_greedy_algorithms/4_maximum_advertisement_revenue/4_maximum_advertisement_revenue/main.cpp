#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
using std::vector;
long long max_dot_product(vector<int> a, vector<int> b) {
  std::sort(a.begin(),a.end());
  std::sort(b.begin(),b.end());
  long long a1;
  long long b1;
  long long result = 0;
  for (size_t i = 0; i < a.size(); i++) {
      a1 =a[i]*1.0;
      b1 = b[i]*1.0;
      result+=a1*b1;
  }
  return result;
}

void test_solution(){
    std::cout<<max_dot_product({23},{39})<<std::endl;
    assert(max_dot_product({23},{39}) == 897);
    std::cout<<max_dot_product({1,3,-5},{-2,4,1})<<std::endl;
    assert(max_dot_product({1, 3, -5},{-2, 4, 1}) == 23);
    std::cout<<max_dot_product({1,3,5},{2,4,1})<<std::endl;
    assert(max_dot_product({1,3, 5},{2, 4, 1}) == 27);
}

int main() {
  test_solution();
  size_t n;
  std::cin >> n;
  vector<int> a(n), b(n);
  for (size_t i = 0; i < n; i++) {
    std::cin >> a[i];
  }
  for (size_t i = 0; i < n; i++) {
    std::cin >> b[i];
  }
  std::cout << max_dot_product(a, b) << std::endl;

}
