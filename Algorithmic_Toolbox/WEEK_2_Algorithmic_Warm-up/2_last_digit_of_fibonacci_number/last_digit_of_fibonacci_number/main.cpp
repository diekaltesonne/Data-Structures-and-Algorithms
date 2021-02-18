#include <iostream>
#include <cassert>

int get_fibonacci_last_digit_naive(int n) {
    if (n <= 1)
        return n;
    int previous = 0;
    int current  = 1;
    for (int i = 0; i < n - 1; ++i) {
        int tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }
    return current % 10;
}


int get_fibonacci_last_digit_fast(int n) {
    int F[n+1];
    F[0]=0;
    F[1]=1;
    for(int i = 2; i<=n; i++){
        F[i]=(F[i-1]+F[i-2])% 10;
    }
    return F[n];
}
void test_solution() {
//    std::cout<< get_fibonacci_last_digit_fast(3)<<std::endl;
//    std::cout<< get_fibonacci_last_digit_naive(3)<<std::endl;
//    std::cout<< get_fibonacci_last_digit_fast(10)<<std::endl;
    assert(get_fibonacci_last_digit_fast(3) == get_fibonacci_last_digit_naive(3));
    assert(get_fibonacci_last_digit_fast(10) == 5);
    for (int n = 0; n < 47; ++n){
        //std::cout<< n<<std::endl;
        assert(get_fibonacci_last_digit_fast(n) == get_fibonacci_last_digit_naive(n));
    }
}


int main() {
    //test_solution();
    //std::cout<<"GOOD"<<std::endl;
    uint n;
    std::cin >> n;
    int c = get_fibonacci_last_digit_fast(n);
    std::cout << c << '\n';
}
