#include <iostream>
#include <cassert>


int get_change(int m) {
  int x_10 =m/10;
  m -= x_10 * 10;

  int x_5 =m/5;
  m -= x_5 * 5;

  int x_1 =m/1;
  m -= x_1 * 1;

  return x_10+x_5+x_1;
}

void test_solution(){
    std::cout<<get_change(2)<<std::endl;
    assert(get_change(2) == 2);
    std::cout <<get_change(28)<< std::endl;
    assert(get_change(28) == 6);
    std::cout<<"GOOD"<<std::endl;
}

int main() {
  //test_solution();
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}
