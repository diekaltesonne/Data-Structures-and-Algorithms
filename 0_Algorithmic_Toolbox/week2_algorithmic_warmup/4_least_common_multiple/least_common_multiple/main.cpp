#include <iostream>
#include <cassert>

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;
  return (long long) a * b;
}

long long gcd_fast(long long a, long long b) {
  if(b==0){
      return a;
  }
  long long remainder = a % b;
  return gcd_fast(b,remainder);
}

long long lcm_fast(int a, int b) {
  return (long long)(a/gcd_fast(a,b))*b;
}

void test_solution(){

    std::cout<<lcm_fast(8,6)<<std::endl;
    assert(lcm_fast(8,6) == lcm_naive(6,8));
    std::cout <<lcm_fast(28851538,1183019)<< std::endl;
    assert(lcm_fast(28851538,1183019) == 1933053046);
    std::cout<<"GOOD"<<std::endl;

}

int main(){
  //test_solution();
  int a, b;
  std::cin >> a >> b;
  if(a>=b){
      std::cout << lcm_fast (a,b)<< std::endl;
  }else{
      std::cout << lcm_fast (b,a) << std::endl;
  }
  return 0;
}
