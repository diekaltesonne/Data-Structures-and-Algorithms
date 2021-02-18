#include <iostream>
#include <vector>
#include <cassert>

using std::cin;
using std::cout;
using std::vector;
using std::max;

int compute_min_refills(int dist, int tank, vector<int>& stops) {
    vector<int> x= {0};
    x.insert(x.end(), stops.begin(), stops.end());
    x.push_back(dist);
    size_t num_Refills = 0;
    size_t current_Refill = 0;
    size_t last_Refill = 0;
    while(current_Refill <= (x.size() - 1)){
        last_Refill = current_Refill;
        while( current_Refill <= ( x.size() - 1 ) && (x[current_Refill+1] - x[last_Refill])<=tank){
              current_Refill+=1;
        }
        if(current_Refill == last_Refill){
            return -1;
        }
        if(current_Refill <= (x.size()-1)){
            num_Refills+=1;
        }
    }
    return num_Refills;
}
//void test_solution(){
//    std::cout<<compute_min_refills(400,250,{100,150})<<std::endl;
//    assert(compute_min_refills(400,250,{100,150})== 1);
//    std::cout<<compute_min_refills(700, 200, {100, 200, 300, 400})<<std::endl;
//    assert(compute_min_refills(700, 200, {100, 200, 300, 400})== -1);
//    std::cout<<compute_min_refills(1000, 200, {100, 200,250, 300, 400, 600,820})<<std::endl;
//    assert(compute_min_refills(1000, 200, {100, 200,250, 300, 400, 600,820})== -1);
//    std::cout<<compute_min_refills(1000, 200, {100, 200,250, 300, 400, 600,800})<<std::endl;
//    assert(compute_min_refills(1000, 200, {100, 200,250, 300, 400, 600,800})== 4);
//    std::cout<<compute_min_refills(10,3, {1,2,5,9})<<std::endl;
//    assert(compute_min_refills(10,3, {1,2,5,9})== -1);
//    std::cout<<compute_min_refills(200,250,{100,150})<<std::endl;
//    assert(compute_min_refills(200,250,{100,150})== 0);
//    std::cout<<compute_min_refills(1200, 400, {200, 375, 550, 750})<<std::endl;
//    assert(compute_min_refills(1200, 400, {200, 375, 550, 750})== -1);
//    std::cout<<compute_min_refills(1150, 400, {200, 375, 550, 750})<<std::endl;
//    assert(compute_min_refills(1150, 400, {200, 375, 550, 750})== 2);
//    std::cout<<"GOOD"<<std::endl;
//}

int main() {
    //test_solution();

    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<int> stops(n);
    for (size_t i = 0; i < n; ++i)
        cin >> stops.at(i);
    std::cout << compute_min_refills(d, m, stops) << "\n";

    return 0;
}
