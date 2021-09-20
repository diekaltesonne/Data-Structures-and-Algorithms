#include <iostream>
#include <cassert>
#include <cmath>
#include <vector>

int fibonacci_sum_naive(long long n) {
    if (n <= 1)
        return n;
    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;
    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
        sum += current;
    }
    return sum % 10;
}

long long fibonacci_sum_fast(long long n) {
    long long sum =0;
    long long  F[n+1];
    F[0] = 0.0;
    F[1] = 1;
    if(n == 0){
        return 0;
    }
    if(n == 1){
        return 1;
    }
    sum+= F[0]+F[1];

    for(size_t i = 2; i <= n; i++){
        F[i]=(F[i-1]+F[i-2])% 10;
        sum+=F[i];
    }
    return sum%10;
}
void test_solution(){
    std::cout<<fibonacci_sum_fast(3)<<std::endl;
    assert(fibonacci_sum_fast(3) == 4);
    std::cout <<fibonacci_sum_fast(100)<< std::endl;
    assert(fibonacci_sum_fast(100) == 5);
    std::cout <<fibonacci_sum_fast(78134)<< std::endl;
    std::cout <<fibonacci_sum_fast(832564823476)<< std::endl;
}
int main(){
    test_solution();
    long long n = 0;
    std::cin >> n;
    std::cout <<fibonacci_sum_fast(n);
}
