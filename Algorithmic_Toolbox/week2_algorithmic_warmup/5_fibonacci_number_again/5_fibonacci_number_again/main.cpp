#include <iostream>
#include <cassert>
#include <cmath>
#include <vector>

long long get_fibonacci_huge_naive(long long n, long long m) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;
    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }
    return current % m;
}

long long get_pisano_period(long long m) {
    long long a = 0, b = 1, c = a + b;
    for (int i = 0; i < m * m; i++) {
        c = (a + b) % m;
        a = b;
        b = c;
        if (a == 0 && b == 1) return i + 1;
    }
}

int get_fibonacci_huge_fast(long long n, long long m) {
    long long period = get_pisano_period(m);
    long long F[period+1];
    F[0]=0;
    F[1]=1;
    for(size_t i = 2; i<=period; i++){
        F[i]= (F[i-1]+F[i-2])%m;
    }

    return F[n%period];
}
void test_solution(){
    std::cout<<get_fibonacci_huge_fast(1,239)<<std::endl;
    assert(get_fibonacci_huge_fast(1 ,239) == 1);
    std::cout <<get_fibonacci_huge_fast(115,1000)<< std::endl;
    assert(get_fibonacci_huge_fast(115,1000) == 885);
    std::cout<<get_fibonacci_huge_fast(2816213588 ,30524)<<std::endl;
    assert(get_fibonacci_huge_fast(2816213588 ,30524) == 10249);
}
int main(){
    //test_solution();
    long long n, m;
    std::cin >> n >> m;
    std::cout << get_fibonacci_huge_fast(n, m) << '\n';

}
  
