#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>
#include <deque>
#include <map>
using std::vector;
using std::map;
using std::pair;
double get_optimal_value(int capacity, vector<int> weights, vector<int> values){
    double value_big = 0 ;
    double c_w = 0 ;
    map<double,pair<int,int>> sorted_v_w;
    for(size_t i = 0 ; i < weights.size(); i++){
        sorted_v_w[((1.0 *values[i])/(1.0 *weights[i]))] = std::make_pair(values[i],weights[i]);
    }
    //std::cout<<sorted_v_w.begin()->second.first<<" " << sorted_v_w.begin()->second.second<<std::endl;
    for (auto iter = sorted_v_w.rbegin(); iter != sorted_v_w.rend(); ++iter) {
        if(capacity == 0){
            return value_big;
        }
        c_w = capacity/ iter->second.second;
        if(c_w>=1){
            capacity  -= iter->second.second;
            value_big += iter->second.first;
        }else{
            //std::cout<<iter->first<<"key"<<std::endl;
            value_big += iter->first*capacity;
            capacity -= capacity;
        }
    }
    return value_big;
}

void test_solution(){
    vector<int> values={60,100,120};
    vector<int> weights = {20,50,30};
    std::cout<<get_optimal_value(50,weights,values)<<std::endl;
    assert(get_optimal_value(50,weights,values) == 180.0000);
    values = {500};
    weights = {30};
    std::cout <<get_optimal_value(10,weights,values)<< std::endl;
    //std::cout <<get_optimal_value(10,weights,values)<< std::endl;
    assert(get_optimal_value(10,weights,values) == 166.6666667);
    std::cout<<"GOOD"<<std::endl;
}

int main() {
  //std::cout.precision(10);
  //test_solution();
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }
  std::cout.precision(10);
  double optimal_value = get_optimal_value(capacity, weights, values);
  std::cout << optimal_value << std::endl;
  return 0;
}
