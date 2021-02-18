#include <iostream>
#include <cassert>
int gcd_naive(int a, int b) {
  int current_gcd = 1;
  for (int d = 2; d <= a && d <= b; d++) {
    if (a % d == 0 && b % d == 0) {
      if (d > current_gcd) {
        current_gcd = d;
      }
    }
  }
  return current_gcd;
}

int gcd_fast(int a, int b) {
  if(b==0){
      return a;
  }
  int remainder = a % b;
  return gcd_fast(b,remainder);
}
void test_solution() {
    assert(gcd_fast(357,234) == gcd_naive(357,234));
    assert(gcd_fast(3918848,1653264) == 61232);
}



int main() {
  //test_solution();
  int a, b;
  std::cin >> a >> b;
  if(a>=b){
      std::cout << gcd_fast(a, b) << std::endl;
  }else{
      std::cout << gcd_fast(b, a) << std::endl;
  }

  return 0;
}
