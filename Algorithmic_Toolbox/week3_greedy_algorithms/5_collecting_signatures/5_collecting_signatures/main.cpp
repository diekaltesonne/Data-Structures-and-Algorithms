#include <algorithm>
#include <iostream>
#include <climits>
#include <vector>

using std::vector;

struct Segment {
  int start, end;
};

vector<int> optimal_points(vector<Segment> &segments) {
  vector<int> points;
  int point = 0;
  int k =0;
  for (auto& i:segments){

      point = i.start;

      for(auto& j:segments){
          if(j.start<= point <=j.end){
            k++;
          }else{

          }
      }

      if(segments.empty()){
          break;
      }
  }
  return points;
}

void test_solution(){
//    std::cout<<optimal_pointst()<<std::endl;
//    assert(optimal_points() == 897);
//    std::cout<<optimal_points()<<std::endl;
//    assert(optimal_points() == 23);
//    std::cout<<optimal_points()<<std::endl;
//    assert(optimal_points() == 27);
}
int main() {
  int n;
  std::cin >> n;
  vector<Segment> segments(n);
  for (size_t i = 0; i < segments.size(); ++i) {
    std::cin >> segments[i].start >> segments[i].end;
  }
  vector<int> points = optimal_points(segments);
  std::cout << points.size() << "\n";
  for (size_t i = 0; i < points.size(); ++i) {
    std::cout << points[i] << " ";
  }
}
